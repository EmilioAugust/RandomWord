import httpx
from fastapi import HTTPException

async def fetch_definition_word(word: str):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    data = response.json()
    all_definitions = []
    all_parts = set()
    all_synonyms = []
    all_antonyms = []
    everything = [all_parts, all_definitions, all_synonyms, all_antonyms]
    try:
        for definit in data:
            for defi in definit['meanings']:
                all_synonyms.append(defi['synonyms'])
                all_antonyms.append(defi['antonyms'])
                all_parts.add(defi['partOfSpeech'])
                for d in defi['definitions']:
                    all_definitions.append(d['definition'])
    except TypeError:
        raise HTTPException(status_code=404, detail='Not found definition')

    return everything