import pandas as pd
import psycopg2


df = pd.read_csv("/opt/airflow/data/clean_orders.csv")


conn = psycopg2.connect(
    host="postgres",
    database="airflow",
    user="airflow",
    password="airflow",
    port=5432
)

cur = conn.cursor()


cur.execute("""
DROP TABLE IF EXISTS public.orders;

CREATE TABLE public.orders(
    order_id INT,
    customer VARCHAR(100),
    product VARCHAR(100),
    amount FLOAT,
    country VARCHAR(100),
    tax FLOAT,
    final_amount FLOAT
);
""")


for _, row in df.iterrows():
    cur.execute(
        """
        INSERT INTO public.orders
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            int(row.order_id),
            row.customer,
            row.product,
            float(row.amount),
            row.country,
            float(row.tax),
            float(row.final_amount)
        )
    )


conn.commit()

cur.close()
conn.close()

print("SUCCESS: Data loaded into PostgreSQL")