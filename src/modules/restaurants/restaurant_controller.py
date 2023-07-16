from fastapi import APIRouter
from src.modules.restaurants.dto.find_restaurant_dto import *
from src.modules.restaurants.restaurant_service import search_restaurant
restaurant = APIRouter()
restaurant = APIRouter(tags=["Restaurants"], prefix="/restaurant")


@restaurant.post('/search')
async def searchRestaurant(rest: FindReetaurant):
        return await search_restaurant(rest)