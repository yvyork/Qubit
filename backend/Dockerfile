FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /django
RUN mkdir ticketpdf
COPY . .
RUN export BROTHER_QL_PRINTER=tcp://192.168.171.217
RUN export BROTHER_QL_MODEL=QL-720NW
RUN pip3 install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
