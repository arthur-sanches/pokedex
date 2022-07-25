from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import (add_pokemon, fetch_all_pokemons, fetch_one_pokemon,
                      remove_pokemon, update_pokemon)
from model import Pokemon

# App object
app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return "Welcome trainer!"


@app.get("/api/pokemon")
async def get_all_pokemon():
    response = await fetch_all_pokemons()
    return response


@app.get("/api/pokemon/{entry}", response_model=Pokemon)
async def get_pokemon_by_entry(entry):
    response = await fetch_one_pokemon(entry)
    if response:
        return response
    raise HTTPException(
        404, f"There is no Pokémon with the Pokédex entry number of {entry}")


@app.post("/api/pokemon", response_model=Pokemon)
async def post_pokemon(pokemon: Pokemon):
    response = await add_pokemon(pokemon.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")


@app.put("/api/pokemon/{entry}&{name}", response_model=Pokemon)
async def put_pokemon(entry: int, name: str):
    response = await update_pokemon(entry, name)
    if response:
        return response
    raise HTTPException(
        404, f"There is no Pokémon with the Pokédex entry number of {entry}")


@app.delete("/api/pokemon/{entry}")
async def delete_pokemon(entry):
    response = await remove_pokemon(entry)
    if response:
        return "Succesfully deleted pokémon!"
    raise HTTPException(
        404, f"There is no Pokémon with the Pokédex entry number of {entry}")
