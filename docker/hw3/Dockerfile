FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
COPY memory_info.py . 

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "memory_info.py"]