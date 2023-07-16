from fastapi import APIRouter
from modules.products.dto.find_product_dto import FindProduct
from modules.products.product_service import *

product = APIRouter()
product = APIRouter(tags=["Products"], prefix="/products")

@product.get('/all/{page}')
async def getProducts(page: int):
    return  await getAllProducts(page)

@product.post('/search')

async def findSimilarProducts(product: FindProduct):
    return await getSimilarProducts(product)

