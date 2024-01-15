FROM python:3.11-slim

COPY . /src
WORKDIR /src

RUN apt update && \
    apt install -y python3-psycopg2 postgresql libpq-dev
RUN pip install -r requirements.txt
RUN chmod +x db_mgmt.sh

EXPOSE 8080

ENTRYPOINT [ "./db_mgm.sh" ]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]