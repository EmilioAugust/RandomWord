from fastapi import APIRouter, HTTPException
from supabase import create_client
from models import Word, LevelWord
from services.services import fetch_definition_word
import json, random, glob
from environs import Env

env = Env()
env.read_env(".env")
router = APIRouter(prefix='/v1')
SUPABASE_URL = env("SUPABASE_URL")
SUPABASE_KEY = env("SUPABASE_KEY")
SUPABASE_BUCKET = env("SUPABASE_BUCKET", "english-words")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

cache = {}

@router.get('/random', response_model=Word)
async def get_random_word():
    try:
        file_name = "english_words.json"
        if file_name not in cache:
            try:
                response = supabase.storage.from_(SUPABASE_BUCKET).download(file_name)
                data = json.loads(response.decode("utf-8"))
                cache[file_name] = data
            except Exception as e:
                raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")

        data = cache[file_name]

        random_word_entry = random.choice(data)
        random_word = random_word_entry["word"]
        everything = await fetch_definition_word(random_word)

        word = Word(word=random_word, part_of_speech=everything[0], definitions=everything[1], synonyms=everything[2], antonyms=everything[3])
        return word

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@router.get('/random/{level}', response_model=LevelWord)
async def get_random_word_by_level(level: str):
    if level.lower() == 'a1':
        file_name = "english_words_a1.json"
        if file_name not in cache:
            try:
                response = supabase.storage.from_(SUPABASE_BUCKET).download(file_name)
                data = json.loads(response.decode("utf-8"))
                cache[file_name] = data
            except Exception as e:
                raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")

        data = cache[file_name]

        random_word_entry = random.choice(data)
        random_word = random_word_entry["word"]
        everything = await fetch_definition_word(random_word)
        level_word = LevelWord(word=random_word, part_of_speech=everything[0], definitions=everything[1], synonyms=everything[2], antonyms=everything[3], level='A1')
    
    elif level.lower() == 'a2':
        file_name = "english_words_a2.json"
        if file_name not in cache:
            try:
                response = supabase.storage.from_(SUPABASE_BUCKET).download(file_name)
                data = json.loads(response.decode("utf-8"))
                cache[file_name] = data
            except Exception as e:
                raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")

        data = cache[file_name]

        random_word_entry = random.choice(data)
        random_word = random_word_entry["word"]
        everything = await fetch_definition_word(random_word)
        level_word = LevelWord(word=random_word, part_of_speech=everything[0], definitions=everything[1], synonyms=everything[2], antonyms=everything[3], level='A2')

    elif level.lower() == 'b1':
        file_name = "english_words_b1.json"
        if file_name not in cache:
            try:
                response = supabase.storage.from_(SUPABASE_BUCKET).download(file_name)
                data = json.loads(response.decode("utf-8"))
                cache[file_name] = data
            except Exception as e:
                raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")

        data = cache[file_name]

        random_word_entry = random.choice(data)
        random_word = random_word_entry["word"]
        everything = await fetch_definition_word(random_word)
        level_word = LevelWord(word=random_word, part_of_speech=everything[0], definitions=everything[1], synonyms=everything[2], antonyms=everything[3], level='B1')

    elif level.lower() == 'b2':
        file_name = "english_words_b2.json"
        if file_name not in cache:
            try:
                response = supabase.storage.from_(SUPABASE_BUCKET).download(file_name)
                data = json.loads(response.decode("utf-8"))
                cache[file_name] = data
            except Exception as e:
                raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")

        data = cache[file_name]

        random_word_entry = random.choice(data)
        random_word = random_word_entry["word"]
        everything = await fetch_definition_word(random_word)
        level_word = LevelWord(word=random_word, part_of_speech=everything[0], definitions=everything[1], synonyms=everything[2], antonyms=everything[3], level='B2')

    elif level.lower() == 'c1':
        file_name = "english_words_c1.json"
        if file_name not in cache:
            try:
                response = supabase.storage.from_(SUPABASE_BUCKET).download(file_name)
                data = json.loads(response.decode("utf-8"))
                cache[file_name] = data
            except Exception as e:
                raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")

        data = cache[file_name]

        random_word_entry = random.choice(data)
        random_word = random_word_entry["word"]
        everything = await fetch_definition_word(random_word)
        level_word = LevelWord(word=random_word, part_of_speech=everything[0], definitions=everything[1], synonyms=everything[2], antonyms=everything[3], level='C1')
    else:
        raise HTTPException(status_code=404, detail=f'Not found level {level}')
    
    return level_word
        