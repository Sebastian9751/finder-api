from fastapi import APIRouter
import pandas as pd
from config.database import cursor
from fuzzywuzzy import fuzz

product = APIRouter()

@product.get('/products/{name_product}')
def findSimilarProducts(name_product: str):
    query = "SELECT * FROM product"
    resp = pd.read_sql_query(query, cursor.connection)

    # Lista para almacenar los productos similares
    similar_products = []

    # Comparar cada producto con el nombre proporcionado
    for index, row in resp.iterrows():
        similarity_score = fuzz.token_set_ratio(name_product, row['name_product'])
        if similarity_score >= 35:  # Puedes ajustar el umbral aquí
            row['similarity_score'] = similarity_score
            similar_products.append(row.to_dict())

    # Ordenar la lista de productos similares por puntaje de similitud en orden descendente
    similar_products = sorted(similar_products, key=lambda x: x['similarity_score'], reverse=True)

    return similar_products
