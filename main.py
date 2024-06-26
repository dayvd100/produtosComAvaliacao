from fastapi import FastAPI
from scraping import getting_products

app = FastAPI()


@app.get("/")
def home():
    return "Home"


@app.get("/produtos")
async def retornar_valores():
    products = getting_products()
    return products
