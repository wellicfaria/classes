from pyspark.sql import SparkSession
from script_exctact import extract
from script_transform import transform
from script_load import load

if __name__ == "__main__":
    spark = SparkSession.builder.appName("ETL").getOrCreate()

    df = extract(spark)

    df_t = transform(df)

    load(df_t, "vendas_transformadas.csv")

