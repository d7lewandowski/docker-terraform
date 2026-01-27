### Question 1. Understanding Docker images

Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.

docker run -it \
    --rm \
    --entrypoint=bash \
    python:3.13

cmd:\
```pip --version```\
pip 25.3

### Question 2. Understanding Docker networking and docker-compose

Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

host: postgres (the container name)
port: 5433 

```
ports:
    - '5433:5432' # (defult port is 80; we map it to port 5433)
```

