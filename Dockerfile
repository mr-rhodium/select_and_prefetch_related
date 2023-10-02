FROM python:3.10.9-alpine
RUN pip install -U pip setuptools wheel 
RUN  pip install pdm 


COPY . /usr/src/app/
WORKDIR /usr/src/app/
RUN pdm install 
RUN pdm run python -m manage makemigrations
RUN pdm run python -m manage migrate
RUN pdm run python -m manage loaddata data.json
RUN pdm run python -m manage collectstatic -v 3 --no-input
EXPOSE 9090
ENTRYPOINT ["pdm", "run", "python", "manage.py"]
CMD ["runserver", "0.0.0.0:9090"]
