FROM python:3.8.17

WORKDIR /api/app

COPY . .

RUN pip update -y

RUN pip install --no-cache-dir -r requirements.txt

CMD python app/main.py