from fastapi import FastAPI
from random_word import random_word

app = FastAPI()
app.include_router(random_word.router)

@app.get('/')
async def main():
    return {'message': "Welcome!"}