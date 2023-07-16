from fastapi import FastAPI
from src.modules.products.products_controller import product
from src.modules.restaurants.restaurant_controller import restaurant

app = FastAPI(
    title="Finder-API",
    description="This api compares the similarity of the provided text string and performs a deep search according to an average.",
)

app.include_router(product)
app.include_router(restaurant)


@app.get("/")
def helloworld():
    return "Hello worl"
