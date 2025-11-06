from fastapi import APIRouter, HTTPException
from models import Word, LevelWord
from services.services import fetch_definition_word
import json
import glob
import random

router = APIRouter(prefix='/v1')

@router.get('/random', response_model=Word)
async def get_random_word():
    path = 'json_files/*.json'
    all_data = []
    for filename in glob.glob(path):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            all_data.append(data)
    words = [item['word'] for item in all_data[0]]
    random_word = random.choice(words)
    everything = await fetch_definition_word(random_word)
    word = Word(word=random_word, part_of_speech=everything[0], definitions=everything[1])
    return word

@router.get('/random/{level}', response_model=LevelWord)
async def get_random_word_by_level(level: str):
    if level.lower() == 'a1':
        path = 'json_files/english_words_a1.json'
        for filename in glob.glob(path):
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
        words = [item['word'] for item in data]
        random_word = random.choice(words)
        everything = await fetch_definition_word(random_word)
        level_word = LevelWord(word=random_word, part_of_speech=everything[0], definitions=everything[1], level='A1')
    
    elif level.lower() == 'a2':
        path = 'json_files/english_words_a2.json'
        for filename in glob.glob(path):
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
        words = [item['word'] for item in data]
        random_word = random.choice(words)
        everything = await fetch_definition_word(random_word)
        level_word = LevelWord(word=random_word, part_of_speech=everything[0], definitions=everything[1], level='A2')

    elif level.lower() == 'b1':
        path = 'json_files/english_words_b1.json'
        for filename in glob.glob(path):
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
        words = [item['word'] for item in data]
        random_word = random.choice(words)
        everything = await fetch_definition_word(random_word)
        level_word = LevelWord(word=random_word, part_of_speech=everything[0], definitions=everything[1], level='B1')

    elif level.lower() == 'b2':
        path = 'json_files/english_words_b2.json'
        for filename in glob.glob(path):
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
        words = [item['word'] for item in data]
        random_word = random.choice(words)
        everything = await fetch_definition_word(random_word)
        level_word = LevelWord(word=random_word, part_of_speech=everything[0], definitions=everything[1], level='B2')

    elif level.lower() == 'c1':
        path = 'json_files/english_words_c1.json'
        for filename in glob.glob(path):
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
        words = [item['word'] for item in data]
        random_word = random.choice(words)
        everything = await fetch_definition_word(random_word)
        level_word = LevelWord(word=random_word, part_of_speech=everything[0], definitions=everything[1], level='C1')
    else:
        raise HTTPException(status_code=404, detail=f'Not found level {level}')
    
    return level_word
        