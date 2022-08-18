FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /django
RUN mkdir ticketpdf
COPY . .
RUN mkdir -p /django/media
RUN pip3 install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
