from fastapi import APIRouter
from modules.products.dto.find_product_dto import *
from modules.products.product_service import *

product = APIRouter()
product = APIRouter(tags=["Products"], prefix="/products")

@product.get('/all', response_model= GetResponse )
async def getProducts(page: int = 1):

    return await getAllProducts(page)


@product.post('/search', response_model= GetResponse)

async def findSimilarProducts(product: FindProduct):
    return await getSimilarProducts(product)

