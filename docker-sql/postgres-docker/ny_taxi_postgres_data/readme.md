Running PostgreSQL in a Container

docker run -it --rm \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  postgres:18

Params: 
-e sets environment variables (user, password, database name)
-v ny_taxi_postgres_data:/var/lib/postgresql creates a named volume
Docker manages this volume automatically
Data persists even after container is removed
Volume is stored in Docker's internal storage
-p 5432:5432 maps port 5432 from container to host
postgres:18 uses PostgreSQL version 18 (latest as of Dec 2025)