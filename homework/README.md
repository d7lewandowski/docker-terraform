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

### Question 3. Counting short trips

```
SELECT COUNT(*) FROM green_tripdata WHERE lpep_pickup_datetime between '2025-11-01' and '2025-12-01' A
 ND trip_distance <= 1;

 +-------+
| count |
|-------|
| 8007  |
+-------+
```
### Question 4. Longest trip for each day

```
 SELECT lpep_pickup_datetime, trip_distance FROM green_tripdata WHERE trip_distance < 100 ORDER BY trip
 _distance DESC LIMIT 5;

 +----------------------+---------------+
| lpep_pickup_datetime | trip_distance |
|----------------------+---------------|
| 2025-11-14 15:36:27  | 88.03         |
| 2025-11-20 12:28:02  | 73.84         |
| 2025-11-23 10:12:18  | 45.26         |
| 2025-11-22 02:07:07  | 40.16         |
| 2025-11-15 14:12:35  | 39.81         |
+----------------------+---------------+
```

### Question 5. Biggest pickup zone
```
 SELECT sum(g.total_amount), z."Zone" FROM green_tripdata g INNER JOIN zones z ON z."LocationID" = g."P
 ULocationID" WHERE g.lpep_pickup_datetime between '2025-11-18' and '2025-11-19' GROUP BY z."Zone" ORDER BY sum(g.total_amount) de
 sc LIMIT 3;

 +--------------------+-------------------+
| sum                | Zone              |
|--------------------+-------------------|
| 9281.919999999996  | East Harlem North |
| 6696.130000000003  | East Harlem South |
| 2378.7899999999995 | Central Park      |
+--------------------+-------------------+
 ```

 For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

 ```
 WITH cte AS 
 (SELECT g.total_amount, z."Zone", g.tip_amount, g."DOLocationID" FROM green_tripdata g INNER JOIN zones z ON z."LocationID" = g."
 PULocationID" WHERE g.lpep_dropoff_datetime between '2025-11-01' and '2025-12-01' AND z."Zone" = 'East Harlem North' ORDER BY g.t
 ip_amount DESC) SELECT c."Zone" AS PICK_UP_LOCATION, c."tip_amount", c."DOLocationID" as DROP_LOCATION, g."Zone" AS ZONE_DROP_LOC
 ATON FROM cte c INNER JOIN zones g ON c."DOLocationID" = g."LocationID" LIMIT 3; 
+-------------------+------------+---------------+-------------------+
| pick_up_location  | tip_amount | drop_location | zone_drop_locaton |
|-------------------+------------+---------------+-------------------|
| East Harlem North | 81.89      | 263           | Yorkville West    |
| East Harlem North | 50.0       | 138           | LaGuardia Airport |
| East Harlem North | 45.0       | 74            | East Harlem North |
+-------------------+------------+---------------+-------------------+
 ```

 ### Question 7. Terraform Workflow

terraform init, terraform apply -auto-approve, terraform destroy