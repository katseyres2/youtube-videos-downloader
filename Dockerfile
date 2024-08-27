FROM python:3.8.19-slim-bullseye
WORKDIR .
RUN apt-get update -y
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "-m", "http.server"]
