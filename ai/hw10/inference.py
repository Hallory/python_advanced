import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def predict_sentiment(text, model_path="./fine_tuned_model", base_model="distilbert-base-multilingual-cased"):
    tokenizer = AutoTokenizer.from_pretrained(base_model)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    
    with torch.no_grad():
        outputs = model(**inputs)
        
    predicted_class = torch.argmax(outputs.logits, dim=1).item()
    return "Позитивный" if predicted_class == 1 else "Негативный"

if __name__ == "__main__":
    review = "Потрясающая атмосфера, этот фильм превзошел все мои ожидания!"
    result = predict_sentiment(review)
    print(f"Текст: '{review}'")
    print(f"Анализ тональности: {result}")