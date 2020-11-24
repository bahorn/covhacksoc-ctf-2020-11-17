FROM python:3.9


WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
