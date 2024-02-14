FROM ubuntu:22.04
RUN apt update && apt install -y python-is-python3 python3-pip

RUN pip install requests==2.23.0 gkeepapi

RUN pip install trello
COPY keepToTrello.py . 
CMD ["python","keepToTrello.py"]
