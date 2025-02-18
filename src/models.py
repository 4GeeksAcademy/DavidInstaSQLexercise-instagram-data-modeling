import os
import sys
import enum
from sqlalchemy import Enum, ForeignKey
from typing import List
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()
class MediaType(enum.Enum):
    VIDEO = "video"
    PHOTO = "photo"
    MUSIC = "music"

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_from_to: Mapped[int] = mapped_column(ForeignKey("user.id"))

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    usser_name: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    second_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    Post: Mapped[List["Post"]] = relationship(back_populates="user")
    Follower: Mapped[List["Follower"]] = relationship(back_populates="follower")
    Comment: Mapped[List["Comment"]] = relationship(back_populates="comment")

class Comment (Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str]  = mapped_column(nullable=False)
    author_id: Mapped[int] = mapped_column(foreign_key=True)
    post_id: Mapped[str] = mapped_column(foreign_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id")) 
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id")) 


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    Comment: Mapped[List["Comment"]] = relationship(back_populates="comment")
    Comment: Mapped[List["Media"]] = relationship(back_populates="media")

class Media (Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[MediaType]  = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)  
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id")) 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
