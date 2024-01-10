


def transform(df):

    df_t = df.withColumn("TotalVendas", df["QuantidadeVendida"] * df["PrecoUnitario"])

    df_t = df_t.select(["ProdutoID", "TotalVendas"])

    df_t = df_t.groupBy("ProdutoID").sum("TotalVendas")

    df_t = df_t.filter(df_t["sum(TotalVendas)"] > 10.0)
    
    return df_t