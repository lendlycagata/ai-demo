FROM python:3.8

EXPOSE 8080

WORKDIR /app

COPY . ./

RUN python -m pip install -r requirements.txt

CMD ["python", "app.py"]