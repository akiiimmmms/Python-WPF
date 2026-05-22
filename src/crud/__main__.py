import uvicorn
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from crud.router.HealthRouter import health_router

app = FastAPI()

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(health_router, prefix="/health", tags=["health"])


def run() -> None:
    kwargs = {
        "app": app,
        "host": "localhost",
        "port": 8000,
        "loop": "asyncio",
        "http": "h11",
    }
    uvicorn.run(**kwargs)


if __name__ == "__main__":
    run()