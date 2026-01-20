**NY Taxi Dataset and Data Ingestion**

uv init
Setting up Jupyter:\
uv add --dev jupyter\
uv run jupyter notebook\
uv add sqlalchemy psycopg2-binary\
uv add tqdm


**Verify the Data**\
Connect to it using pgcli:

uv run pgcli -h localhost -p 5432 -u root -d ny_taxi