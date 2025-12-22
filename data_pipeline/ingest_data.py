import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]


def ingest_data(
        url: str,
        engine,
        table_name: str,
        chunksize: int = 100000,
) -> pd.DataFrame:
    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunksize
    )

    first_chunk = next(df_iter)

    first_chunk.head(0).to_sql(
        name=table_name,
        con=engine,
        if_exists="replace"
    )

    print(f"Table {table_name} created")

    first_chunk.to_sql(
        name=table_name,
        con=engine,
        if_exists="append"
    )

    print(f"Inserted first chunk: {len(first_chunk)}")

    for df_chunk in tqdm(df_iter):
        df_chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists="append"
        )
        print(f"Inserted chunk: {len(df_chunk)}")

    print(f'done ingesting to {table_name}')

def main():
    pg_user = 'root'
    pg_pass = 'root'
    pg_host = 'localhost'
    pg_port = '5432'
    pg_db = 'ny_taxi'
    year = 2021
    month = 1
    chunksize = 100000
    table_name = 'new_york_taxi_table'

    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')
  
    data_source = "https://raw.githubusercontent.com/marita-kube/data_engineering_project/main/taxi_tripdata_{year:04d}-{month:02d}.csv.gz"


    ingest_data(
        data_source=data_source,
        engine=engine,
        table_name=table_name,
        chunksize=chunksize
    )

if __name__ == '__main__':
    main()