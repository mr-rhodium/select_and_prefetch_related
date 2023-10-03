# Django DB Optimization

The simple project for article on medium

You can using Dockerfile or pull up git repo and install project in local environmen

# Docker

build

`docker build --no-cache -t myapp . `

run

`docker run -it --rm  -p 9090:9090 myapp `

# or without Docker

`git clone `

`pdm install `
`RUN pdm run python -m manage makemigrations`
`RUN pdm run python -m manage migrate`
`RUN pdm run python -m manage loaddata data.json`
`RUN pdm run python -m manage collectstatic -v 3 --no-input`

`pdm run manage.py runserver `
