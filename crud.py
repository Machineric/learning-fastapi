from sqlalchemy.orm import Session 

import models, schemas 


def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(
        models.Movie.id == movie_id
    ).first()
    

def get_movie_by_title(db: Session, title: str):
    return db.query(models.Movie).filter(
        models.Movie.title == title
    ).first()
    
    
def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Movie).offset(skip).limit(limit).all()


def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def delete_movie_by_id(db: Session, movie_id: int):
    db_movie = db.query(models.Movie).filter_by(id=movie_id)
    db_movie.delete()
    db.commit()
    

def update_movie_by_id(db: Session, movie_id: int, movie: schemas.MovieUpdate):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    db_movie.title = movie.title
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie