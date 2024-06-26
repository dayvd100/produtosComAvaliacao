from fastapi import FastAPI
from scraping import getting_products

app = FastAPI()


@app.get("/")
async def retornar_valores():
    products = getting_products()
    return {"products": products}
