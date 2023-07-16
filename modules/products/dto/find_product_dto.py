from pydantic import BaseModel

class FindProduct(BaseModel):
    name_product: str
