FROM python:2.7
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org Flask
ENV NAME Alireza
CMD ["python", "app.py"]
