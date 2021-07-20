from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, oauth2
from ..database import get_db
from ..repository import blog


router = APIRouter(prefix='/blog', tags=['Blogs'])


@router.get('', response_model=List[schemas.ShowBlog])
def show_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show_all(db)


@router.get('/{id}', response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)


@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db, current_user)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def change(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.change(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def disintegrate(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.disintegrate(id, db)