#!/usr/bin/node
function main () {
  const N = parseInt(process.argv[2]);

  if (isNaN(N)) {
    console.log(1);
    return;
  }

  const FACTORIAL = fact(N);

  console.log(FACTORIAL);
}
function fact (N) {
  let result = 1;

  for (let i = 1; i <= N; i++) {
    result *= i;
  }
  return result;
}
main();
