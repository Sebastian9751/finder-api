from fastapi import APIRouter
from modules.products.get_products_dto import GetProducts


from modules.products.product_service import getSimilarProducts

product = APIRouter()

@product.post('/products')

async def findSimilarProducts(product: GetProducts):
    return await getSimilarProducts(product)