import pandas as pd


df=pd.read_csv(
    "/opt/airflow/data/raw_orders.csv"
)


df["tax"] = df["amount"]*0.18


df["final_amount"] = (
    df["amount"] + df["tax"]
)


df.to_csv(
    "/opt/airflow/data/clean_orders.csv",
    index=False
)


print("Transformation done")