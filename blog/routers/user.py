from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..repository import user


router = APIRouter(prefix='/user', tags=['Users'])


@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
    return user.show_user(id, db)


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)
