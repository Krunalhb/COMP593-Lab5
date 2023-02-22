import sys
from datetime import datetime, timedelta
from pastebin_api import create_paste
from poke_api import get_pokemon_info   

def get_pokemon_name():
    """
    Gets the Pokémon name from the command line parameter

    Returns:
    str: The Pokémon name
    """
    if len(sys.argv) < 2:
        print("Error: Please provide a Pokémon name as a command line parameter.")
        sys.exit(1)
    return sys.argv[1]

def create_paste_title_and_body(pokemon_info):
    """
    Constructs the title and body text for the new paste.

    Args:
    pokemon_info (dict): A dictionary containing information about the Pokémon.

    Returns:
    tuple: A tuple containing the title and body text for the new paste.
    """
    name = pokemon_info['name'].capitalize()
    abilities = pokemon_info['abilities']
    abilities_list = [ability['ability']['name'] for ability in abilities]
    abilities_str = '\n'.join(abilities_list)
    title = f"{name}'s Abilities"
    body = '- ' + abilities_str.replace('\n', '\n- ')
    return title, body

def main():
    # Get the Pokémon name from the command line parameter
    pokemon_name = get_pokemon_name()

    # Fetch Pokémon information from the PokéAPI
    pokemon_info = get_pokemon_info(pokemon_name)
    if not pokemon_info:
        print(f"Error: Failed to fetch Pokémon information for {pokemon_name}.")
        sys.exit(1)

    # Construct the title and body text for the new paste
    title, body = create_paste_title_and_body(pokemon_info)

    # Create the new PasteBin paste
    paste_url = create_paste(title, body, '1M', '0')
    if not paste_url:
        print("Error: Failed to create new PasteBin paste.")
        sys.exit(1)

    # Print the URL of the new PasteBin paste
    print(f"New PasteBin paste created: {paste_url}")

if __name__ == '__main__':
    main()

