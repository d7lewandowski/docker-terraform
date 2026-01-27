#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import click 


## Load data by pandas to load to db postgres by chunks with size of 100000
## Method 1
@click.command()
@click.option('--user', default='postgres', help='PostgreSQL user')
@click.option('--password', default='postgres', help='PostgreSQL password')
@click.option('--host', default='postgres', help='PostgreSQL host')
@click.option('--port', default=5433, type=int, help='PostgreSQL port')
@click.option('--db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--table', default='green_tripdata', help='Target table name')
def ingest_data_green_tripdata(user, password, host, port, db, table):

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Ingestion logic here
    df_iter = pd.read_parquet(
        filepath_or_buffer='green_tripdata_2025-11.parquet',
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=100000
    )

    first = True

    for df_chunk in df_iter:

        if first:
            # Create table schema (no data)
            df_chunk.head(0).to_sql(
                name="yellow_taxi_data",
                con=engine,
                if_exists="replace"
            )
            first = False
            print("Table created")

        # Insert chunk
        df_chunk.to_sql(
            name="yellow_taxi_data",
            con=engine,
            if_exists="append"
        )

        print("Inserted:", len(df_chunk))

## Load data by pandas to load to db postgres by chunks with size of 100000
## Method 1
@click.command()
@click.option('--user', default='postgres', help='PostgreSQL user')
@click.option('--password', default='postgres', help='PostgreSQL password')
@click.option('--host', default='postgres', help='PostgreSQL host')
@click.option('--port', default=5433, type=int, help='PostgreSQL port')
@click.option('--db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--table', default='taxi_zone_lookup', help='Target table name')
def ingest_data_taxi_zone_lookup(user, password, host, port, db, table):

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Ingestion logic here
    df_iter = pd.read_csv(
        filepath_or_buffer='taxi_zone_lookup.csv',
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=100000
    )

    first = True

    for df_chunk in df_iter:

        if first:
            # Create table schema (no data)
            df_chunk.head(0).to_sql(
                name="yellow_taxi_data",
                con=engine,
                if_exists="replace"
            )
            first = False
            print("Table created")

        # Insert chunk
        df_chunk.to_sql(
            name="yellow_taxi_data",
            con=engine,
            if_exists="append"
        )

        print("Inserted:", len(df_chunk))



if __name__ == '__main__':
    ingest_data_green_tripdata()
    ingest_data_taxi_zone_lookup()

    print('taxi_zone_lookup END!')

