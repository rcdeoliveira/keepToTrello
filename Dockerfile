FROM rcdeoliveira/gkeepapi

RUN pip install trello
COPY keepToTrello.py . 
CMD ["python","keepToTrello.py"]
