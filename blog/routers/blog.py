from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from blog.database import get_db

from .. import database, models, schemas
from ..repository import blog

router = APIRouter(
    tags=['blogs'],
    prefix="/blog"
)

## posting something in db
@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:  schemas.Blog, db: Session= Depends(database.get_db)):
    return blog.create(request,db)


# get all from the db
@router.get("/",response_model=List[schemas.showBlog])
def get_blog( db: Session= Depends(database.get_db)):
    return blog.get_all(db)

# get particular blog
@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.showBlog)
def show(id:int,db: Session= Depends(get_db)):
   return blog.show(id,db)

## deleting a blog from the db
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int,db: Session= Depends(get_db)):
    return blog.delete(id,db)


# updating a blog
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request: schemas.Blog,db: Session= Depends(get_db)):
    return blog.update(id,request,db)