import pandas as pd
import random
import os
from datetime import datetime, timedelta

def generate_data(n=48):
    t0 = datetime.now() - timedelta(hours=n)
    data = []

    for i in range(n):
        ts = t0 + timedelta(hours=i)
        imps = random.randint(1000, 5000)
        clicks = int(imps * random.uniform(0.01, 0.05))
        convs = int(clicks * random.uniform(0.1, 0.3))
        cost = round(imps * random.uniform(0.5, 2.0), 2)
        data.append([ts, imps, clicks, convs, cost])

    df = pd.DataFrame(data, columns=["timestamp", "impressions", "clicks", "conversions", "cost"])
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/data.csv", index=False)
    print("✔️ Data generated")

if __name__ == "__main__":
    generate_data()
