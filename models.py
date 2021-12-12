from sqlalchemy import (
    Boolean, 
    Column, 
    ForeignKey, 
    Integer, 
    String, 
    Date,
)

from database import Base

class Movie(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    release_date = Column(Date)
    
    
    
    