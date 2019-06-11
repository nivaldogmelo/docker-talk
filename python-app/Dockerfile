FROM debian:stable

RUN apt-get update && apt-get install python3 python3-pip -y

RUN pip3 install flask requests

EXPOSE 5000

COPY main.py /main.py

CMD ["python3", "main.py"]
