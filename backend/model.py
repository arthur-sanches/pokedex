from pydantic import BaseModel


class Pokemon(BaseModel):
    entry: int
    name: str
