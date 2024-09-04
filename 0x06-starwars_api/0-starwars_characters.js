#!/usr/bin/env python3
"""
This script prints all characters of a Star Wars movie.
The first positional argument passed is the Movie ID.
Example: 3 = "Return of the Jedi"
It displays one character name per line in the same order as the "characters" list in the /films/ endpoint.
You must use the Star Wars API.
"""

import sys
import requests

def get_characters(movie_id):
    # SWAPI base URL
    base_url = f"https://swapi.dev/api/films/{movie_id}/"
    
    try:
        # Make a request to the Star Wars API to get movie details
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the JSON response
        movie_data = response.json()
        
        # Fetch the list of characters' URLs
        character_urls = movie_data.get("characters", [])
        
        # Iterate over each character URL and fetch the character's name
        for url in character_urls:
            char_response = requests.get(url)
            char_response.raise_for_status()
            char_data = char_response.json()
            print(char_data.get("name"))
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py <Movie ID>")
        sys.exit(1)
    
    movie_id = sys.argv[1]
    
    get_characters(movie_id)
