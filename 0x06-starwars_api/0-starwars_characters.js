#!/usr/bin/node
/**
 * This script prints all characters of a Star Wars movie.
 * The first positional argument passed is the Movie ID.
 * It displays one character name per line in the same order as the "characters" list in the /films/ endpoint.
 * You must use the Star Wars API.
 */

const axios = require('axios');

// Function to get characters based on Movie ID
async function getCharacters(movieId) {
  // SWAPI base URL
  const baseUrl = `https://swapi.dev/api/films/${movieId}/`;

  try {
    // Make a request to the Star Wars API to get movie details
    const response = await axios.get(baseUrl);

    // Fetch the list of characters' URLs
    const characterUrls = response.data.characters;

    // Iterate over each character URL and fetch the character's name
    for (const url of characterUrls) {
      const charResponse = await axios.get(url);
      console.log(charResponse.data.name);
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }
}

// Main execution block
if (process.argv.length !== 3) {
  console.error('Usage: ./star_wars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

getCharacters(movieId);
