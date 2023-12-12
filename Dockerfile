FROM ubuntu:latest
RUN apt update
RUN apt install python3 python3-pip -y
WORKDIR /diabetes_project
COPY requirements.txt requirements.txt
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 3000
CMD ["python3", "./app.py"]