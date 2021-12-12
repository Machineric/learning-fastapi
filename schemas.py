from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    release_date: Optional[date]
    

class MovieCreate(MovieBase):
    
    class Config:
        orm_mode = True


class MovieUpdate(MovieBase):
    
    class Config:
        orm_mode = True


class Movie(MovieBase):
    id: int
    
    class Config:
        orm_mode = True
        
