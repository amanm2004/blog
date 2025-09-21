
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from blog.database import get_db

from .. import schemas
from ..repository import user

router = APIRouter(
    tags=["users"],
    prefix="/user"
)

#creating a user
@router.post('/create',status_code=status.HTTP_201_CREATED,response_model=schemas.showUser)
def create(request: schemas.User,db: Session= Depends(get_db)):
     return user.create(request,db)
   


#getting a user
@router.get('/get/{id}',response_model=schemas.showUser)
def showuser(id:int,db: Session= Depends(get_db)):
    return user.show(id,db)