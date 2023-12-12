FROM python:3.9-slim-buster
WORKDIR /diabetes_project
COPY requirements.txt requirements.txt
COPY . .
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python ./app.py