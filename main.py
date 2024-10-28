from fastapi import FastAPI, HTTPException, status
from database import create_db_and_tables, SessionDep
from models import MoviesModel
from random import randint
from sqlmodel import select
from schemas import MovieSchema

app = FastAPI()

create_db_and_tables()

@app.post("/movies")
async def create_movie(movie_data: MovieSchema, database: SessionDep):
    movie = MoviesModel(
        nombre_pelicula=movie_data.nombre_pelicula,
        año_estreno=movie_data.año_estreno,
        duracion=movie_data.duracion,
        director=movie_data.director,
        clasificacion=movie_data.clasificacion,
        genero=movie_data.genero   
    )
    
    database.add(movie)
    database.commit()
    database.refresh(movie)
    return movie
"""
GET- Obtener algo
POST - crear algo
PUT- Actualizar algo
DELETE - Eliminar

"""
@app.get("/movies")
async def get_movies(database: SessionDep):
    statement = select(MoviesModel)
    results = database.exec(statement)
    items = results.all()
    return items

@app.get("/movies/{movie_id}")
async def get_user_by_id(movie_id: int,database: SessionDep):
    movie = database.get(MoviesModel, movie_id)
    
    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Pelicula no encontrada")
    
    return movie
#! crear una tabla donde registrar peliculas, nombre, duracion, director