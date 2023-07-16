from fastapi import FastAPI
from modules.products.products_controller import product
from modules.restaurants.restaurant_controller import restaurant

app = FastAPI(
    title="Finder-API",
    description="This api compares the similarity of the provided text string and performs a deep search according to an average.",
)

app.include_router(product)
app.include_router(restaurant)


@app.get("/")
def helloworld():
    return "Hello worl"
