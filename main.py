from fastapi import FastAPI
from fastapi.responses import FileResponse
from random_word import router

app = FastAPI()
app.include_router(router)
favicon_path = 'favicon/favicon.ico'

@app.get('/')
async def main():
    return {'message': "Welcome!"}

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)