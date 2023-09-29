from fastapi import FastAPI
import asyncio
import uvicorn

from config import VERSION


app = FastAPI(title="Stock Watcher API", description="Stock Watcher API", version=VERSION, summary="API Endpoints",)

@app.get("/", tags=['API Endpoints'])
def get_root(msg="API is working fine..."):
    return msg

async def main():
    config = uvicorn.Config("main:app", host="localhost", port=5000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())