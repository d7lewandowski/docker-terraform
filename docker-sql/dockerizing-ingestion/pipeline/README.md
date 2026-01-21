### Dockerfile

Explanation
FROM python:3.13.11-slim: Start with slim Python 3.13 image for smaller size\
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/: Copy uv binary from official uv image\
WORKDIR /code: Set working directory inside container\
ENV PATH="/code/.venv/bin:$PATH": Add virtual environment to PATH\
COPY pyproject.toml .python-version uv.lock ./: Copy dependency files first (better caching)\
RUN uv sync --locked: Install all dependencies from lock file (ensures reproducible builds)\
COPY ingest_data.py .: Copy ingestion script\
ENTRYPOINT ["python", "ingest_data.py"]: Set entry point to run the ingestion script

### Build the Docker Image:

Folder -> pipeline and then invoke next cli command 
```
docker build -t taxi_ingest:v001 .
```


### Containerized ingestion
```
docker run -it \
  --network=pg-network \
  taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --table=yellow_taxi_trips
```