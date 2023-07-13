FROM python:3.8.17

WORKDIR /api/app

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

CMD python /api/app/main.py