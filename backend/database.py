# MongoDB Driver
import motor.motor_asyncio

from model import Pokemon

client = motor.motor_asyncio.AsyncIOMotorClient("connection for mongodb here")
database = client.Pokedex
collection = database.Pokedex


async def fetch_one_pokemon(entry):
    document = await collection.find_one({"entry": int(entry)})
    return document


async def fetch_all_pokemons():
    pokemons = []
    cursor = collection.find({})
    async for document in cursor:
        pokemons.append(Pokemon(**document))
    return pokemons


async def add_pokemon(pokemon):
    document = pokemon
    result = await collection.insert_one(document)
    return document


async def update_pokemon(entry, name):
    await collection.update_one({"entry": int(entry)}, {"$set": {"name": name}})
    document = await collection.find_one({"entry": int(entry)})
    return document


async def remove_pokemon(entry):
    await collection.delete_one({"entry": int(entry)})
    return True
