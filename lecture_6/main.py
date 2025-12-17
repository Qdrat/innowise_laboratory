from fastapi import FastAPI

app = FastAPI()

@app.get('/healthcheck')
async def healthcheck() -> dict:
    return {'status' : 'ok'}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app="main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )