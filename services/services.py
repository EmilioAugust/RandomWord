import httpx

async def fetch_definition_word(word: str):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    data = response.json()
    all_definitions = []
    try:
        for definit in data:
            for defi in definit['meanings']:
                for d in defi['definitions']:
                    all_definitions.append(d['definition'])
    except TypeError:
        return {'error': "Couldn't find definition"}

    return all_definitions