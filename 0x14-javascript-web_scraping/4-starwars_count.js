#!/usr/bin/node
/**
 * Prints the number of movies where the character “Wedge Antilles” is present.
 */

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    results.forEach(result => {
      const characters = result.characters;
      characters.forEach(character => {
        if (character.endsWith('18/')) { count++; }
      });
    });
    console.log(count);
  }
});
