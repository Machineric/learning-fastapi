# uvicorn main:app --reload

from typing import List, Dict

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session 

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
        

@app.get('/movies', response_model=List[schemas.Movie])
def read_movies(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> List[models.Movie]:
    movies = crud.get_movies(db, skip=skip, limit=limit)
    return movies
    

@app.post('/movies', response_model=schemas.Movie, status_code=201)
def create_movie(
    movie: schemas.MovieCreate, db: Session = Depends(get_db)
) -> models.Movie:
    db_movie = crud.get_movie_by_title(db, title=movie.title)
    if db_movie:
        raise HTTPException(
            status_code=400,
            detail='Movie already exists.'
        )
    return crud.create_movie(db=db, movie=movie)
    

@app.get('/movies/{movie_id}', response_model=schemas.Movie)
def read_movie_item(
    movie_id: int, db: Session = Depends(get_db)
) -> models.Movie:
    db_movie = crud.get_movie(db, movie_id=movie_id)
    return db_movie

    
@app.delete('/movies/{movie_id}', status_code=204)
def delete_movie_item(
    movie_id: int, db: Session = Depends(get_db)
) -> Dict[str, str]:
    crud.delete_movie_by_id(db, movie_id=movie_id)
    return { 'message': 'successfully deleted.' }


@app.put('/movies/{movie_id}', response_model=schemas.Movie)
def update_movie_item(
    movie_id: int, movie: schemas.MovieUpdate, db: Session = Depends(get_db)
) -> models.Movie:
    db_movie = crud.update_movie_by_id(db, movie_id=movie_id, movie=movie)
    return db_movie