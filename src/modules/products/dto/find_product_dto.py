from pydantic import BaseModel


class FindProduct(BaseModel):
    name_product: str


## Just for response example


class Product(BaseModel):
    id_product: int
    name_product: str
    description_product: str
    image_product_url: str
    price: float


class Restaurant(BaseModel):
    id_restaurant: int
    name_restaurant: str
    restaurant_img_url: str


class Item(BaseModel):
    product: Product
    restaurant: Restaurant


class GetResponse(BaseModel):
    info: dict
    result: list[Item]
