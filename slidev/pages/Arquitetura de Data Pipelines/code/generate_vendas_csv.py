import pandas as pd
import random
from datetime import date, timedelta

def generate_date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def create_vendas_csv(filename, num_days=30, num_products=20):
    start_date = date.today() - timedelta(days=num_days)
    end_date = date.today()

    data = []
    for single_date in generate_date_range(start_date, end_date):
        for product_id in range(1, num_products + 1):
            quantidade = random.randint(1, 20)
            preco = round(random.uniform(10.0, 100.0), 2)
            data.append([single_date, product_id, quantidade, preco])

    df = pd.DataFrame(data, columns=['Data', 'ProdutoID', 'QuantidadeVendida', 'PrecoUnitario'])
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    create_vendas_csv("vendas.csv")
