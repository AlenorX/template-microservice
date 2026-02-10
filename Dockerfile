FROM python:3.11-alpine

WORKDIR /template-microservice

COPY . .

RUN cd app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app",  "--host 0.0.0.0", "--port 80"]