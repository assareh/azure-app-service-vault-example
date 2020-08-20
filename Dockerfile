FROM python:3.7-slim

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY application.py ./application.py

EXPOSE 5000
ENTRYPOINT ["python", "application.py"]