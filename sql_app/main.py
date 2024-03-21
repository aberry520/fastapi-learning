
from operator import or_
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models

from . import schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), name: str = None, email: str = None, postalzip: str = None):
    if name:
        users = crud.get_user_by_name(db, name)
        return users
    if email:
        users = crud.get_user_by_email(db, email)
        return users
    if postalzip:
        users = crud.get_user_by_postalzip(db, postalzip)
        return users
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), name: str = None):
#     query = db.query(models.User)
#     if name:
#         query = query.filter(or_(models.User.name.ilike(f"%{name}%")))
#     users = query.offset(skip).limit(limit).all()
#     return users

@app.get("/items")
def read_item():
    return {"message": "Items"}
