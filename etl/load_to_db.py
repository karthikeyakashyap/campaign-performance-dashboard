import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DB_URI = os.getenv("DB_URI")
engine = create_engine(DB_URI)

df = pd.read_csv("data/data.csv", parse_dates=["timestamp"])
df.to_sql("campaign_metrics", engine, if_exists="append", index=False)
print("✔️ Loaded to PostgreSQL")
