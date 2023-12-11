#!/usr/bin/node
const number = parseInt(process.argv[2]);

(isNaN(number)) ? console.log('Not a number') : console.log(`My number: ${number}`);
