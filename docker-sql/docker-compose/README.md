### docker-compose

- allows us to launch multiple containers using a single configuration file, so that we don't have to run multiple complex docker run commands separately
- Docker compose makes use of YAML files

File: 

```
services:
  pgdatabase:
    image: postgres:18
    environment:
      POSTGRES_USER: "root"
      POSTGRES_PASSWORD: "root"
      POSTGRES_DB: "ny_taxi"
    volumes:
      - "ny_taxi_postgres_data:/var/lib/postgresql"
    ports:
      - "5432:5432"

  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: "admin@admin.com"
      PGADMIN_DEFAULT_PASSWORD: "root"
    volumes:
      - "pgadmin_data:/var/lib/pgadmin"
    ports:
      - "8085:80"



volumes:
  ny_taxi_postgres_data:
  pgadmin_data:
```


Docker-compose takes care of network, every container "service" will run within the same network and will be able to find each other accoring to their names (in this case: pgdatabase and pgadmin)

### Start services with docker-compose
We can run Docker compose by running following cli from the same dirctory where docker-compose.yaml is found. 
```
docker-compose up
```
### Detached Mode (thus freeing up your terminal)
```
docker-compose up -d
```

### Stop Services (terminal Ctrl+C) in order to shutdown the containers
```
docker-compose down
```

### Handful commands 
```
# View logs
docker-compose logs

# Stop and remove volumes
docker-compose down -v
```

### Benefits of Docker Compose
- Running all services by one line command 
- built-in network creation 
- Configuration managment
- Declarative infrastuructre 


### Running the Ingestion Script with Docker Compose 

If you want to re-run the dockerized ingest script when you run Postgres and pgAdmin with docker-compose, you will have to find the name of the virtual network that Docker compose created for the containers.

```
# check the network link:
docker network ls

# it's pipeline_default (or similar based on directory name)
# now run the script:
docker run -it \
  --network=docker-compose_default \
  taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --table=yellow_taxi_trips
```
