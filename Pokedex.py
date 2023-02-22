import poke_api

pokemon_info = poke_api.get_pokemon_info("MewTwo")
if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"Type(s): {[t['type']['name'] for t in pokemon_info['types']]}")
    print(f"Abilities: {[a['ability']['name'] for a in pokemon_info['abilities']]}")
else:
    print("Failed to fetch Pokémon information.")
