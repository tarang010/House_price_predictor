import snowflake.connector
import pandas as pd
from src.utils.helpers import load_yaml
print("Loading the YAML file...")
config = load_yaml("src/config/config.yaml")
sf = config["snowflake"]
print("Loaded successfully")
print("Connecting to Snowflake account...")
conn = snowflake.connector.connect(
    user=sf["user"],
    password=sf["password"],
    account=sf["account"],
    warehouse=sf["warehouse"],
    database=sf["database"],
    schema=sf["schema"]
)
print("Connected Successfully!")
print("Extracting data from Snowflake...")
query = f"SELECT * FROM {sf['table']}"
cursor = conn.cursor()
cursor.execute(query)
df = cursor.fetch_pandas_all()
df.to_csv("data/raw/house_data.csv", index=False)
print("Data from Snowflake extracted successfully!")
cursor.close()
conn.close()