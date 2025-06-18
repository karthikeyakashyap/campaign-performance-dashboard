import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv("DB_URI"))

df = pd.read_sql("SELECT * FROM campaign_metrics ORDER BY timestamp", engine)
df["CTR"] = df["clicks"] / df["impressions"]

mean = df["CTR"].mean()
std = df["CTR"].std()
threshold = mean - 2 * std

anomalies = df[df["CTR"] < threshold]

print("📉 Anomalies detected:")
print(anomalies)
