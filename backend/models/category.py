from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from backend.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=250), nullable=False)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name is required")
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not name.strip():
            raise ValueError("Name can't be empty")
        if len(name) > 100:
            raise ValueError("Name can't be more than 100 characters")
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not description:
            raise ValueError("Description is required")
        if not isinstance(description, str):
            raise ValueError("Description must be a string")
        if not description.strip():
            raise ValueError("Description can't be empty")
        if len(description) > 250:
            raise ValueError("Description can't be more than 250 characters")
        return description
