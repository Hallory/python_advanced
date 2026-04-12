# Обязательно к выполнению
# Обработать таймауты

# Реализовать retry-механизм с tenacity


# Дополнительно (по желанию)
# Получить эмбеддинги двух разных текстов и сравнить их.

# Реализовать простой поиск похожих текстов.

import os
import time
import numpy as np
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
timeout_seconds = 30
timeout_ms = timeout_seconds * 1000
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=timeout_ms))

model_name="gemini-2.5-flash"

documents = [
    "Python — идеальный язык для обучения нейросетей",
    "Разработка серверной части требует знаний баз данных",
    "Искусственный интеллект меняет мир программирования",
    "Создание быстрых API на FastAPI набирает популярность"
]
class APITimeoutError(Exception):
    pass

class RateLimitError(Exception):
    pass

@retry(
    wait=wait_exponential(multiplier=1, min=1, max=10), 
    stop=stop_after_attempt(3), 
    retry=retry_if_exception_type((APITimeoutError, RateLimitError)),
    reraise=True
    )
def get_gemini_response(prompt):
    time.sleep(1)
    try:
        response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            http_options=types.HttpOptions(timeout=timeout_ms)
            )
        )
        return response.text
    except Exception as e:
        error_message = str(e).lower()
        if any(word in error_message for word in ["timeout", "deadline", "exceeded"]):
            if "429" in error_message or "quota" in error_message:
                raise RateLimitError(f"Лимиты закончились: {e}")
            raise APITimeoutError(f"API запрос отвалился по времени: {e}")
        else:
            raise e
    


def get_embedding(text):
    result = client.models.embed_content(
        model='gemini-embedding-2-preview',
        contents=text,
    )
    return result.embeddings[0].values


def get_similarities(text1, text2):
    v1 = np.array(get_embedding(text1))
    v2 = np.array(get_embedding(text2))
    d = np.linalg.norm(v1) * np.linalg.norm(v2)
    if not d:
        return 0.0
    return np.dot(v1, v2) / d

def find_similar(query, docs):
    results = []
    for doc in docs:
        score = get_similarities(query, doc)
        results.append((doc, score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results[0]


if __name__ == "__main__":
    model_name = "gemini-2.5-flash" 

    print("--- 1. Тестируем генерацию текста (и Retry) ---")
    try:
        answer = get_gemini_response("Напиши короткий слоган для курса по Python.")
        print(f"Ответ AI: {answer}")
    except Exception as e:
        print(f"Не удалось получить ответ: {e}")

    print("\n--- 2. Тестируем сравнение двух текстов ---")
    t1 = "Я люблю кодить на питоне"
    t2 = "Программирование на Python приносит мне удовольствие"
    score = get_similarities(t1, t2)
    print(f"Схожесть '{t1}' и '{t2}': {score:.4f}")

    print("\n--- 3. Тестируем семантический поиск ---")
    user_query = "веб-сервер и базы данных"
    
    best_match, best_score = find_similar(user_query, documents)
    
    print(f"Ваш запрос: {user_query}")
    print(f"Самый подходящий текст: {best_match}")
    print(f"Оценка схожести: {best_score:.4f}")