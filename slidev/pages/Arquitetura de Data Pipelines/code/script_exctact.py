

def extract(spark):
    df = spark.read.csv("vendas.csv", header=True, inferSchema=True)
    return df