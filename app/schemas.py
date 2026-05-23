from pydantic import BaseModel

# Schemas - used to validate the data that is sent to the server
class PostCreate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    title: str
    content: str

