#!/usr/bin/node
function main () {
  const charToPrint = 'X';
  const SIZE = parseInt(process.argv[2]);

  // Verify SIZE
  if (isNaN(SIZE)) {
    console.log('Missing size');
    return -1;
  }

  printSquare(SIZE, charToPrint);
}
function printSquare (SIZE, charToPrint) {
  for (let i = 0; i < SIZE; i++) {
    let output = '';
    for (let j = 0; j < SIZE; j++) {
      output += charToPrint;
    }
    console.log(output);
  }
}
main();
