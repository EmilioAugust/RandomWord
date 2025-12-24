from fastapi import FastAPI
from fastapi.responses import FileResponse
from random_word import router

app = FastAPI()
app.include_router(router)

@app.get('/')
async def main():
    return {'message': "Welcome!"}
