FROM python:3.9-slim-buster
WORKDIR /diabetes_project
COPY requirements.txt requirements.txt
COPY . .
RUN pip install -r requirements.txt
CMD [ "python3","app.py"]
ENV PORT=80