#!/usr/bin/node
const fs = require('fs');

function main () {
  if (process.argv.length - 2 !== 3) {
    return;
  }

  const fromOne = process.argv[2];
  const fromTwo = process.argv[3];
  const to = process.argv[4];

  append(fromOne, to);
  append(fromTwo, to);
}
function append (from, to) {
  fs.readFile(from, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    fs.appendFile(to, data, (err, data) => {
      if (err) {
        console.log(err);
      }
    });
  });
}
main();
