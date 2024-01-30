#!/usr/bin/node
/**
 * Prints the number of movies where the character “Wedge Antilles” is present.
 */

const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];
const fs = require('fs');

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileName, body, 'utf-8', error => {
      if (error) {
        console.log(error);
      }
    });
  }
});
