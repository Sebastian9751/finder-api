from fastapi import APIRouter
import pandas as pd
from config.database import cursor


product = APIRouter()

@product.get('/products')
def findAll():
    query = "SELECT * FROM product"
    resp = pd.read_sql_query(query, cursor.connection)

    print(resp)
    return resp.to_dict(orient='records')


