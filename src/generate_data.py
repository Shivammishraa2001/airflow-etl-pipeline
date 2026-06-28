from faker import Faker
import pandas as pd
import random
import os


fake = Faker()

os.makedirs("/opt/airflow/data", exist_ok=True)


records=[]

for i in range(100):

    records.append({
        "order_id": i+1,
        "customer": fake.name(),
        "product": fake.word(),
        "amount": random.randint(100,5000),
        "country": fake.country()
    })


df=pd.DataFrame(records)


df.to_csv(
    "/opt/airflow/data/raw_orders.csv",
    index=False
)


print("Data generated")