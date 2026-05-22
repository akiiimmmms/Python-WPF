from fastapi import Response
from crud.service import NotFoundException
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from crud.router.HealthRouter import health_router
from crud.router.BaumRouter import baum_router

app = FastAPI()

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(baum_router, prefix="/baum", tags=["baum"])

@app.exception_handler(NotFoundException)
def not_found_exception_handler(request, exc):
    return Response(status_code=404, content=str(exc))

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