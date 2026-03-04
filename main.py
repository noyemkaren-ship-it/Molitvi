from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates
from hristos import mol, molitvi

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "k": "☦"
        })

@app.get("/smol")
async def smol(request: Request):
    return templates.TemplateResponse("smol.html", {
        "request": request,
        "mol": mol
    })

@app.get("/church")
async def church(request: Request):
    return templates.TemplateResponse("church.html", {
        "request": request,
        "molitva": molitvi,
        "k": "☦"
    })
