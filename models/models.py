from pydantic import BaseModel

class Word(BaseModel):
    word: str
    part_of_speech: list | None = None
    definitions: list | None = None
    synonyms: list | None = None
    antonyms: list | None = None

class LevelWord(BaseModel):
    word: str
    part_of_speech: list | None = None
    definitions: list | None = None
    synonyms: list | None = None
    antonyms: list | None = None
    level: str

