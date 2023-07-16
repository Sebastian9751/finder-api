from pydantic import BaseModel


class GetProducts(BaseModel):
    name_product: str
