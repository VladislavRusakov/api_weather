import json
from fastapi import FastAPI, Response, Form
from data import get_data_from_weather_api


app = FastAPI()


@app.get("/")
def index_page():
    """Рендер главной страницы"""
    with open('templates/index.html', 'r') as f:
        index_page = f.read()
    return Response(index_page, media_type='text/html')


@app.post("/api")
def data_from_frontend_form(city: str = Form(...)):
    """"""
    try:
        response = get_data_from_weather_api(city)
        print(response)
        return Response(json.dumps(response), media_type='text/html')
    except KeyError:
        return Response("<h1>Incorrect city name</h1>", media_type='text/html')



@app.get("/api/{pk}")
def api_response(pk: str):
    """"""
    city = pk
    try:
        response = get_data_from_weather_api(city)
        print(response)
        return Response(json.dumps(response), media_type='text/html')
    except KeyError:
        return Response("<h1>Incorrect city name</h1>", media_type='text/html')