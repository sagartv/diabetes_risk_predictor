FROM python:3.8-slim-buster
WORKDIR /diabetes_project
COPY requirements.txt requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
RUN pip install -r requirements.txt
ENV PORT=80