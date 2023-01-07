from pydantic import BaseModel, EmailStr


class GetUserResponseSchema(BaseModel):
    greeting: str


class PostUserBodySchema(BaseModel):
    username: str
    email: EmailStr
