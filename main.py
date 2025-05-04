from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/', summary='Пробная ручка', tags=['Основные ручки'])
async def home():
    return f'For the Emperor!'

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
