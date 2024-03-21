from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from .database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "mytable"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=True)
    phone = Column(String(100), nullable=True)
    email = Column(String(255), nullable=True)
    address = Column(String(255), nullable=True)
    postalzip = Column(String(100), nullable=True)
    region = Column(String(50), nullable=True)
    country = Column(String(100), nullable=True)

    # items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")