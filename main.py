from fastapi import FastAPI
import pandas as pd 
import pyarrow.parquet as pq
import joblib

app = FastAPI()


@app.get("/developer/")
def developer(desarrollador: str):
    



@app.get("/eveloper_reviews_analysis/")
def developer_reviews_analysis(desarrolladora: str):




@app.get("/userdata/")
def userdata(user_id: str):



@app.get("/UserForGenre/")
def obtener_informacion_por_genero(genero: str):


@app.get("/best_developer_year/")
def best_developer_year(año: int):



@app.get("/prediccion")
def recomendacion(juego:str):


@app.get("/UserForGenre/")
def obtener_informacion_por_genero(genero: str):
