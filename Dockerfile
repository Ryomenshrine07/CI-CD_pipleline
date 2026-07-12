FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install flask

EXPOSE 8000

ENV FLASK_APP=app.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]
