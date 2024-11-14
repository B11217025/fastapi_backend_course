FROM python:3.11

WORKDIR /code

COPY ./requiremrnts.txt /code/requiremrnts.txt
RUN pip install --no-cache-dir --upgrade -r /code/requiremrnts.txt


COPY ./app /code/app

CMD ["fastapi","run","app/main.py","--port","80"]
