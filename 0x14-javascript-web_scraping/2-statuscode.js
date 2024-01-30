#!/usr/bin/node
/**
 * Make a request and prints the status code
 */

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) { console.log(error); } else { console.log(`code: ${response && response.statusCode}`); }
});
