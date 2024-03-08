import logging

# -------------------------------------- #
from fastapi import FastAPI, Request



app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.get('/api')
async def root(request: Request):
    return {}