import requests

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2"

def get_pokemon_info(pokemon):
    """
    Fetches information for a specified Pokémon from the PokéAPI.

    Args:
        pokemon (str or int): The name or Pokédex number of the Pokémon to fetch.
    
    Returns:
        dict: A dictionary containing all the Pokémon information fetched from the PokéAPI, if retrieved
        successfully. Returns None if the Pokémon information is not fetched successfully.
    """
    pokemon = str(pokemon).strip().lower()

    # Construct the API URL for the specified Pokémon
    url = f"{POKEAPI_BASE_URL}/pokemon/{pokemon}"

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        pokemon_info = response.json()
        return pokemon_info
    else:
        print(f"Error: Failed to fetch information for Pokémon '{pokemon}'. Status code: {response.status_code}")
        return None
