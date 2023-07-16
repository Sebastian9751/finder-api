import pandas as pd
from fuzzywuzzy import fuzz
from unidecode import unidecode
from config.database import engine
from modules.restaurants.dto.find_restaurant_dto import FindReetaurant

SIMILARITY_SCORE_VALUE = 37
async def search_restaurant(rest: FindReetaurant):
    query = "EXEC GetRestaurantWithLikes"
    conn = engine.connect()
    res = pd.read_sql_query(query, conn)
    name_restaurant_normalized = unidecode(rest.name_restaurant)
    similar_restaurants = []

    for index, row in res.iterrows():
        row_name_normalized = unidecode(row["name_restaurant"])
        similarity_score = fuzz.token_set_ratio(
            name_restaurant_normalized, row_name_normalized
        )
        if similarity_score >= SIMILARITY_SCORE_VALUE:
            similar_restaurants.append(row)

    return similar_restaurants
