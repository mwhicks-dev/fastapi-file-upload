import uvicorn

from src.demo import app

if __name__ == '__main__':
    uvicorn.run(
        app,
        host="0.0.0.0",
        reload=False
    )
