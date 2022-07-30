FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /t_mobApp
COPY requirements.txt /t_mobApp/requirements.txt
RUN pip install -r requirements.txt
COPY . /t_mobApp
