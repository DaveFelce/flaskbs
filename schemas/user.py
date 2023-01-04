from pydantic import BaseModel


class UserQueryResponseSchema(BaseModel):
    greeting: str
