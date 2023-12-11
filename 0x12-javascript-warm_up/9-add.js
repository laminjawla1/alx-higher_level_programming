#!/usr/bin/node
function main () {
  const n1 = parseInt(process.argv[2]);
  const n2 = parseInt(process.argv[3]);

  console.log(add(n1, n2));
}
function add (n1, n2) {
  return n1 + n2;
}
main();
