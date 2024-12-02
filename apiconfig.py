from pydantic import BaseModel

class ModelStory(BaseModel):
    user: int
    text: str

