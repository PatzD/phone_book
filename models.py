from pydantic import BaseModel, EmailStr, validator
from uuid import UUID, uuid4
from typing import Optional

class Contact(BaseModel):
    id: Optional[UUID] = None
    name: str
    surname: str
    phone_number: int
    email: EmailStr

    @validator('id', pre=True, always=True)
    def set_default_id(cls, v):
        return v or uuid4()
    
    @validator('id')
    def validate_unique_id(cls, v, values):
        if v and v in [contact.id for contact in values.get('contacts', [])]:
            raise ValueError('ID must be unique')
        return v