from fastapi import FastAPI
from modules.products.products_controller import product
app = FastAPI()

app.include_router(product)
@app.get("/")
def helloworld():
    return "Hello worl"

