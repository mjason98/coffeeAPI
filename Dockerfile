from alpine:3.18.2

WORKDIR /app

run apk update
run apk add python3 py3-pip

copy requirements.txt .
copy services .
copy app.py .

run ls -l
run ls services/

run pip3 install -r requirements.txt

cmd ["python3", "-m", "gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
