from pydantic import BaseModel

class MovieSchema(BaseModel):
    nombre_pelicula: str
    año_estreno: str
    duracion: str
    director: str
    clasificacion: str
    genero: str
    
    