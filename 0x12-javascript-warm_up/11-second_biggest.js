#!/usr/bin/node
function main () {
  const numbers = getNumbers(process.argv);

  if (numbers.length < 2) {
    console.log(0);
    return;
  }

  numbers.sort();
  console.log(numbers[numbers.length - 2]);
}
function getNumbers (list) {
  const numbers = [];
  const len = list.length;

  for (let i = 2; i < len; i++) {
    numbers.push(parseInt(list[i]));
  }
  return numbers;
}
main();
