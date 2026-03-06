from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates
from hristos import mol, molitvi
from iisus import info, info1

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

@app.get("/iisus")
async def church(request: Request):
    return templates.TemplateResponse("iisus.html", {
        "request": request,
        "k": "☦",
        "info": info
    })

@app.get("/earth_create1")
async def earht_history(Request: Request):
    return templates.TemplateResponse("earth.html", {
        "request": Request,
        "title": "1 история",
        "zagalovor": "Создания земли",
        "info1": info1[0]})


@app.get("/earth_create2")
async def earht_history2(Request: Request):
    return templates.TemplateResponse("earth.html", {
        "request": Request,
        "title": "2 история",
        "zagalovor": "Создания людей",
        "info1": info1[1]})


@app.get("/earth_create3")
async def earht_history(Request: Request):
    return templates.TemplateResponse("earth.html", {
        "request": Request,
        "title": "3 история",
        "zagalovor": "Миссей",
        "info1": info1[2]})


@app.get("/isto")
async def root(request: Request):
    return templates.TemplateResponse(
        "isto.html",
        {
            "request": request,
            "k": "☦"
        })
