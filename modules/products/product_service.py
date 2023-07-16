import pandas as pd
from fuzzywuzzy import fuzz
from unidecode import unidecode
from config.database import engine
from modules.products.dto.find_product_dto import *

PAGE_SIZE = 19


def create_product_dict(row):
    return {
        "id_product": row["id_product"],
        "name_product": row["name_product"],
        "description_product": row["description_product"],
        "image_product_url": row["image_product_url"],
        "price": row["price"],
    }


def create_restaurant_dict(row):
    return {
        "id_restaurant": row["id_restaurant"],
        "name_restaurant": row["name_restaurant"],
        "restaurant_img_url": row["restaurant_img_url"],
    }


async def getSimilarProducts(name_product: FindProduct) -> GetResponse:
    query = "EXEC getAllProductsNoPage"
    conn = engine.connect()
    resp = pd.read_sql_query(query, conn)

    similar_products = []
    name_product_normalized = unidecode(name_product.name_product)

    for index, row in resp.iterrows():
        row_name_normalized = unidecode(row["name_product"])
        similarity_score = fuzz.token_set_ratio(
            name_product_normalized, row_name_normalized
        )
        if similarity_score >= 37:
            product_dict = create_product_dict(row)
            restaurant_dict = create_restaurant_dict(row)
            product_with_restaurant_dict = {
                "product": product_dict,
                "restaurant": restaurant_dict,
                "similarity_score": similarity_score,
            }
            similar_products.append(product_with_restaurant_dict)

    similar_products = sorted(
        similar_products, key=lambda x: x["similarity_score"], reverse=True
    )

    return GetResponse(info={"products_found": len(similar_products)}, result=similar_products)


async def getAllProducts(page_number: int) -> GetResponse:
    page_number = max(page_number, 1)
    query = f"EXEC getAllProducts  @PageNumber = {page_number}, @PageSize = {PAGE_SIZE}"
    conn = engine.connect()
    resp = pd.read_sql_query(query, conn)

    products_with_restaurants = [
        {"product": create_product_dict(row), "restaurant": create_restaurant_dict(row)}
        for _, row in resp.iterrows()
    ]

    results = len(products_with_restaurants)
    if results == 0:
        return GetResponse(info={"error": "There is nothing here"}, result=[])

    page_info_dict = {"page_number": page_number, "current_count": len(resp)}

    return GetResponse(info=page_info_dict, result=products_with_restaurants)
