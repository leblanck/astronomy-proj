FROM python:3-alpine

WORKDIR /app
COPY ./astronomy_proj .

RUN pip install -r requirements.txt

ENV ASTRO_ID=""
ENV ASTRO_SECRET=""


USER 1001

CMD python solar.py