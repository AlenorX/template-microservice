FROM python:3.11-alpine

WORKDIR /template-microservice

COPY . .

RUN pip install -r req.txt

EXPOSE 8080

CMD ["uvicorn", "main:app",  "--host 127.0.0.1", "--port 8000"]