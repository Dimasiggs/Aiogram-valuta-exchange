FROM python:3.11

WORKDIR /app

COPY . /app


RUN pip3 install -r requirements.txt
RUN

CMD ["python3", "bot.py"]