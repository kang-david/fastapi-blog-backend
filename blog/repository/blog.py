from fastapi import status, HTTPException, Depends
from sqlalchemy.orm import Session

from .. import schemas, models, oauth2


def show_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with id {id} does not exist'
        )
    return blog


def create(
    request: schemas.Blog,
    db: Session,
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        creator_id=db.query(models.User).filter(models.User.email == current_user['email']).first().id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return 'Blog created successfully'


def change(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with id {id} does not exist'
        )
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return 'Blog updated successfully'


def disintegrate(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Blog with id {id} does not exist'
        )
    blog.delete()
    db.commit()
    return 'Blog deleted successfully'
