# FROM python:3.7.3
FROM python:alpine3.7

ENV PYTHONDONTWRITEBYTECODE 1
# ENV FLASK_APP "app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /app


COPY . /app
WORKDIR /app
# RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
