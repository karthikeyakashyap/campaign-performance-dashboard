import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv("DB_URI"))

df = pd.read_sql("SELECT * FROM campaign_metrics ORDER BY timestamp", engine)
df["CTR"] = df["clicks"] / df["impressions"]

plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["CTR"], marker="o", label="CTR")
plt.axhline(df["CTR"].mean(), color="green", linestyle="--", label="Mean CTR")
plt.axhline(df["CTR"].mean() - 2 * df["CTR"].std(), color="red", linestyle="--", label="Anomaly Threshold")
plt.title("CTR Over Time")
plt.xlabel("Time")
plt.ylabel("Click-Through Rate (CTR)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
