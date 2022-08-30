
FROM python:3.8

ADD main.py .

RUN pip install numpy pandas

CMD ["python", "./main.py"]


#ENV PYTHONDONTWRITEBYTHECODE=true