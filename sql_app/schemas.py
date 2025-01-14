from pydantic import BaseModel

# class ItemBase(BaseModel):
#     title: str
#     description: str | None = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


class UserBase(BaseModel):
    name: str
    phone: str
    email: str
    address: str
    postalzip: str
    region: str
    country: str


# class UserCreate(UserBase):
#     # password: str


class User(UserBase):
    id: int
    # is_active: bool
    # items: list[Item] = []

    class Config:
        orm_mode = True