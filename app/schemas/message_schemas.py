from pydantic import BaseModel


class MessageSchemas(BaseModel):
    message: str
