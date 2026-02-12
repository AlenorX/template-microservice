FROM python:3.11-alpine

WORKDIR /template-microservice

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app .

EXPOSE 80

CMD ["uvicorn", "main:app",  "--host 0.0.0.0", "--port 80"]