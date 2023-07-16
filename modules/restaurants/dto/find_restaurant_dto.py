from pydantic import BaseModel


class FindReetaurant(BaseModel):
    name_restaurant: str

