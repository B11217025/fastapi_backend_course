...
from sqlalchemy import Column, Date, Integer, String, Boolean
from database import Base
...

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    due_data = Column(Date, nullable=True)

class User(Base):
    __tablename__ = "Wu_Yi_Chen"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)