#!/usr/bin/node
/**
 * Reads and prints the contents of a file
 */
const fs = require('fs');
const fileName = process.argv[2];

fs.readFile(fileName, 'utf-8', (error, data) => {
  if (error) { console.log(error); } else { console.log(data); }
});
