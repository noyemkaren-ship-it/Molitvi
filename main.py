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
async def earth_history1(request: Request):
    return templates.TemplateResponse("earth.html", {
        "request": request,
        "title": "1 история",
        "zagalovor": "Сотворение земли",
        "info1": info1[0],
        "part": 1,
        "total": 8
    })

@app.get("/earth_create2")
async def earth_history2(request: Request):
    return templates.TemplateResponse("earth.html", {
        "request": request,
        "title": "2 история",
        "zagalovor": "Сотворение людей",
        "info1": info1[1],
        "part": 2,
        "total": 8
    })

@app.get("/earth_create3")
async def earth_history3(request: Request):
    return templates.TemplateResponse("earth.html", {
        "request": request,
        "title": "3 история",
        "zagalovor": "Грехопадение",
        "info1": info1[2],
        "part": 3,
        "total": 8
    })

@app.get("/earth_create4")
async def earth_history4(request: Request):
    return templates.TemplateResponse("earth.html", {
        "request": request,
        "title": "4 история",
        "zagalovor": "Каин и Авель",
        "info1": info1[3],
        "part": 4,
        "total": 8
    })

@app.get("/earth_create5")
async def earth_history5(request: Request):
    return templates.TemplateResponse("earth.html", {
        "request": request,
        "title": "5 история",
        "zagalovor": "От Адама до Ноя",
        "info1": info1[4],
        "part": 5,
        "total": 8
    })

@app.get("/earth_create6")
async def earth_history6(request: Request):
    return templates.TemplateResponse("earth.html", {
        "request": request,
        "title": "6 история",
        "zagalovor": "Ной и потоп",
        "info1": info1[5],
        "part": 6,
        "total": 8
    })

@app.get("/earth_create7")
async def earth_history7(request: Request):
    return templates.TemplateResponse("earth.html", {
        "request": request,
        "title": "7 история",
        "zagalovor": "Вавилонская башня",
        "info1": info1[6],
        "part": 7,
        "total": 8
    })

@app.get("/earth_create8")
async def earth_history8(request: Request):
    return templates.TemplateResponse("earth.html", {
        "request": request,
        "title": "8 история",
        "zagalovor": "Авраам и обетование",
        "info1": info1[7],
        "part": 8,
        "total": 8
    })

@app.get("/insto")
async def root(request: Request):
    return templates.TemplateResponse(
        "insto.html",
        {
            "request": request,
            "k": "☦"
        })