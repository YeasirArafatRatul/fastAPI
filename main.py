"""
This main.py file was created for dummy practicing
"""

# 1. Import
import uvicorn
from fastapi import FastAPI
from models import Blog

# 2. Create FastAPI instance
app = FastAPI()

# 3. Decorate
# '/' means base url
# If we don't decorate this it will create 'Not Found' Error

# Path/Endpoint/Url
# get/put/post/delete - are called operation
@app.get('/')
def index():
    """Path Operation Function"""
    return {'data': {'name':'Ratul','age':25}}


# Path Operation Decorator
@app.get('/about')
def about():
    """Path Operation Function"""
    return {'data': {'first_name':'Arafat','last_name':'Ratul'}}


# Query Parameter
@app.get('/blogs/')
def all_blogs(limit=10,published:bool= True ):
    print(published)
    # only get 10 published blogs
    if published:
        return {'data':f'{limit} published blogs from the blogs list'}

    return {'data':f'{limit} blogs from the blogs list'}


@app.get('/blogs/unpublished/')
def unpublished():
    return {'data': 'unpublished blog list'}


# Path Parameter
@app.get('/blog-details/{id}')
def blog_details(id:int):
    # print(type(id))
    # fetch blog with id = id
    return {'data':id}



@app.get('/blog-details/{id}/comments')
def comments(id: int):
    # fetch comments of blog with id = id
    return {'data': {'commnet_1':"Good", "comment_2":"Nice"}}



# Request Body

@app.post('/add-blogs')
def create_blog(request:Blog):
    return {'data':f'A blog is created named {request.title}'}


# to change the default port

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)