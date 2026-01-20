### pgAdmin - Database anagement Tool

### Run pgAdmin Container

```
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \ # volume mapping saves pgAdmin settings (server conncetions, preferences)
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -v pgadmin_data:/var/lib/pgadmin \
  -p 8085:80 \ # default port is 80; we map it to 8085 in our localhost to avoid any possible conflicts. 
  dpage/pgadmin4 # actual image name
```


### Docker Networks 

Virtual Docker network called pg-network:
```
docker network create pg-network # to create
docker network rm pg-network # to remove 
```

### Run Containers on the Same Network

```
# Run PostgreSQL on the network
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql \
  -p 5432:5432 \
  --network=pg-network \
  --name pgdatabase \
  postgres:18

# In another terminal, run pgAdmin on the same network
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
      -v pgadmin_data:/var/lib/pgadmin \
        -p 8085:80 \
          --network=pg-network \
            --name pgadmin \
              dpage/pgadmin4
```

- We specify a network and a name for pgAdmin 
- The container names pgdatabase and pgadmin allow the containers to find each other within the network. 