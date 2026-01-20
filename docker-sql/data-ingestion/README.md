## **NY Taxi Dataset and Data Ingestion**

uv init
Setting up Jupyter:\
uv add --dev jupyter\
uv run jupyter notebook\
uv add sqlalchemy psycopg2-binary\
uv add tqdm


### **Verify the Data**\
Connect to it using pgcli:

uv run pgcli -h localhost -p 5432 -u root -d ny_taxi


### **Convert Notebook to Script**

uv run jupyter nbconvert --to=script notebook.ipynb


### Running the Script 
The script reads data in chunks to handle large files efficiently without running out of memory

Example: 
uv run python data_ingestion_db.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table=yellow_taxi_trips