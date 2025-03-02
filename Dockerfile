FROM python:3.11

EXPOSE 8080

WORKDIR /app_etl

ENV PYTHONUNBUFFERED=1

COPY . .

RUN python -m pip install -r requirements.txt

RUN adduser -u 5678 --disabled-password --gecos "" app_etl && chown -R app_etl /app_etl
USER app_etl

RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]
