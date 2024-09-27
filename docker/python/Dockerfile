FROM python:latest

COPY requirements.txt ./

RUN apt update && apt install -y netcat-traditional && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --no-cache-dir -r requirements.txt
