import pandas as pd
from fuzzywuzzy import fuzz
from unidecode import unidecode
from config.database import engine
from modules.products.dto.find_product_dto import FindProduct

async def getSimilarProducts(name_product: FindProduct):
    query = "EXEC getAllProducts"
    conn = engine.connect()
    resp = pd.read_sql_query(query, conn)

    # Lista para almacenar los productos similares
    similar_products = []

    # Convertir el nombre proporcionado a su forma sin acentos
    name_product_normalized = unidecode(name_product.name_product)

    # Comparar cada producto con el nombre proporcionado
    for index, row in resp.iterrows():
        # Convertir el nombre del producto en la fila a su forma sin acentos
        row_name_normalized = unidecode(row['name_product'])
        similarity_score = fuzz.token_set_ratio(name_product_normalized, row_name_normalized)
        if similarity_score >= 37:  # Puedes ajustar el umbral aquí
            # Crear un diccionario con las propiedades del producto
            product_dict = {
                "id_product": row['id_product'],
                "name_product": row['name_product'],
                "description_product": row['description_product'],
                "image_product_url": row['image_product_url'],
                "price": row['price']
            }

            # Crear un diccionario con las propiedades del restaurante
            restaurant_dict = {
                "id_restaurant": row['id_restaurant'],
                "name_restaurant": row['name_restaurant'],
                "restaurant_img_url": row['restaurant_img_url']
            }

            # Combinar los diccionarios en un diccionario final
            product_with_restaurant_dict = {
                "product": product_dict,
                "restaurant": restaurant_dict,
                "similarity_score": similarity_score
            }

            similar_products.append(product_with_restaurant_dict)

    # Ordenar la lista de productos similares por puntaje de similitud en orden descendente
    similar_products = sorted(similar_products, key=lambda x: x['similarity_score'], reverse=True)

    return similar_products


async def getAllProducts(page_number : int):
    PAGE_SIZE = 10
    query = f"EXEC getAllProducts  @PageNumber = {page_number}, @PageSize = {PAGE_SIZE}"
    conn = engine.connect()
    resp = pd.read_sql_query(query, conn)

    products_with_restaurants = []  # Lista para almacenar los productos con restaurantes

    for index, row in resp.iterrows():
        product_dict = {
            "id_product": row['id_product'],
            "name_product": row['name_product'],
            "description_product": row['description_product'],
            "image_product_url": row['image_product_url'],
            "price": row['price']
        }
        restaurant_dict = {
            "id_restaurant": row['id_restaurant'],
            "name_restaurant": row['name_restaurant'],
            "restaurant_img_url": row['restaurant_img_url']
        }

        product_with_restaurant_dict = {
            "product": product_dict,
            "restaurant": restaurant_dict
        }

        products_with_restaurants.append(product_with_restaurant_dict)  # Agregar el diccionario a la lista
        
    page_data ={"page_number": page_number}
    products_with_restaurants.append(page_data)
    return products_with_restaurants  # Devolver la lista de productos con restaurantes


