FROM python:3.8

WORKDIR /app

COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt

COPY . .

COPY main.py auto.py ./Provider ./Interface ./Entity ./Controller ./


CMD ["python", "./main.py"]