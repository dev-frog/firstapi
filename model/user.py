
from pydantic import BaseModel, Field
from beanie import Document

class UserModel(BaseModel):
    username: str
    email: str
    full_name: str = Field(default=None)


class UserDocument(Document, UserModel):
    class Meta:
        collection = "user"