from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..schemas import ShowBlog, Blog, ShowUser, User
from .. import models
from ..repository import blogs
from .oauth2 import get_current_user



router = APIRouter(tags=['blogs'])


@router.get('/all-blogs',response_model=List[ShowBlog])
def all(db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blogs.get_all(db)



# Depends converts Session into Pydantic 
@router.post('/add-blog',status_code=status.HTTP_201_CREATED)
def create_blog(request:Blog, db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@router.get('/blog/{id}',response_model=ShowBlog)
def blog_detail(id, response:Response,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id = {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with id = {id} is not available"}
    return blog




"""
response_model defines what type of response we need. 
response_model = Blog means that we need response as same as 'Blog' model (Pydantic Model / Schema)
"""
# It is actually bulk update
@router.put('/update-blog/{id}',response_model=Blog)
def update_blog(id, request:Blog, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).update(id,request)
    print("BLOG",blog)
    # if not blog.first():
    #     HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Not Found")

    db.commit()
    return "update"


# Delete Blog

# Depends converts Session into Pydantic 
@router.delete('/delete-blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'Done'


