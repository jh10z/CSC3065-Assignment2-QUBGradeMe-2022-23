FROM python:3.11.0
WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
COPY ./config ./config

CMD [ "python3", "-m" , "flask", "--app", "./src/main", "run", "--host=0.0.0.0"]