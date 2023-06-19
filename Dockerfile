from alpine:3.18.2

WORKDIR /app

run apk update
run apk add python3 py3-pip

copy requirements.txt .
copy services services
copy app.py .

run pip3 install -r requirements.txt
run echo -e "DB_NAME=coffee.db\nDB_USER_NAME=user\nDB_USER_PWD=ea654541-426a-409c-a1b3-4597a0ecbfee" > .env



cmd ["python3", "-m", "gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
