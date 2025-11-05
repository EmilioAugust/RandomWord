from pydantic import BaseModel

class Word(BaseModel):
    word: str
    definitions: list | None = None

class LevelWord(BaseModel):
    word: str
    definitions: list | None = None
    level: str

