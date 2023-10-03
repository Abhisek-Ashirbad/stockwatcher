# ============================================================================= 
#-*- coding: utf-8 -*-
# =============================================================================
# Created By  : Abhisek Ashirbad Sethy
# Created On  : 29/09/2023
# © Copyright by Abhisek Ashirbad Sethy
# =============================================================================

# Imports
from fastapi import FastAPI
import asyncio
import uvicorn

from config import HOST, PORT, VERSION, LOG_LEVEL


# App configuration
app = FastAPI(title="Stock Watcher API", description="Stock Watcher API", version=VERSION, summary="API Endpoints",)

# Root API endpoint
@app.get("/", tags=['API Endpoints'])
def get_root(msg="API is working fine..."):
    return msg

# ASGI server configuration
async def main():
    config = uvicorn.Config("main:app", host=HOST, port=PORT, log_level=LOG_LEVEL, reload=True)
    server = uvicorn.Server(config)
    await server.serve()

# App execution starts here...
if __name__ == "__main__":
    asyncio.run(main())