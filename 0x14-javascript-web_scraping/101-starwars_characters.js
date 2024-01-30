#!/usr/bin/node
/**
 * Prints all characters in a movie
 */

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    movie.characters.forEach(character => {
      request.get(character, (error, response, info) => {
        if (error) { console.log(error); } else { console.log(JSON.parse(info).name); }
      });
    });
  }
});
