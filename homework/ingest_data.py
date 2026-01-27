#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import click 

## Load data by pandas to load to db postgres by chunks with size of 100000
## Method 1
'''
docker built -t test:001 .


docker run -it --rm \
  -e POSTGRES_USER="postgres" \
  -e POSTGRES_PASSWORD="postgres" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5433:5432 \
  postgres:18

uv run pgcli -h localhost -p 5433 -u postgres -d ny_taxi


uv run python ingest_data.py \
  --user=postgres \
  --password=postgres \
  --host=localhost \
  --port=5433 \
  --db=ny_taxi \
  --table=green_tripdata \
  --path=/workspaces/docker-terraform/homework/green_tripdata_2025-11.parquet \
  --format=parquet

  uv run python ingest_data.py \
  --user=postgres \
  --password=postgres \
  --host=localhost \
  --port=5433 \
  --db=ny_taxi \
  --table=zones \
  --path=/workspaces/docker-terraform/homework/taxi_zone_lookup.csv \
  --format=csv
'''
@click.command()
@click.option('--user', default='postgres', help='PostgreSQL user')
@click.option('--password', default='postgres', help='PostgreSQL password')
@click.option('--host', default='localhost', help='PostgreSQL host')
@click.option('--port', default=5433, type=int, help='PostgreSQL port')
@click.option('--db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--table', default='green_tripdata', help='Target table name')
@click.option('--path', default='', help='path to file to loda data')
@click.option('--format', default='parquet', help='parquet or csv')
def ingest_data(user, password, host, port, db, table, path, format):

    print(user, password, host, port, db, table, path, format)
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    if format == 'parquet':
        # Ingestion logic here
        df_iter = pd.read_parquet(
            str(path),
        )
        first = True
        if first:
            # Create table schema (no data)
            df_iter.head(0).to_sql(
                name=table,
                con=engine,
                if_exists="replace"
            )
            first = False
            print("Table created")

        # Insert chunk
        df_iter.to_sql(
            name=table,
            con=engine,
            if_exists="append"
        )

    else:
            # Ingestion logic here
        df_iter = pd.read_csv(
            str(path),
            iterator=True,
            chunksize=100000
        )

        first = True

        for df_chunk in df_iter:

            if first:
                # Create table schema (no data)
                df_chunk.head(0).to_sql(
                    name=table,
                    con=engine,
                    if_exists="replace"
                )
                first = False
                print("Table created")

            # Insert chunk
            df_chunk.to_sql(
                name=table,
                con=engine,
                if_exists="append"
            )

            print("Inserted:", len(df_chunk))

    



if __name__ == '__main__':
    ingest_data()
    print('END!')