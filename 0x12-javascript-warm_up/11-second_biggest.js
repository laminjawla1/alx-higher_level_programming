#!/usr/bin/node
function main () {
  const numbers = process.argv.slice(2).map(Number);

  if (numbers.length < 2) {
    console.log(0);
    return;
  }

  numbers.sort((x, y) => {
    return y - x;
  });

  console.log(numbers[1]);
}
main();
