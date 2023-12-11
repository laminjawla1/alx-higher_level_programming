#!/usr/bin/node
function main () {
  const argv = process.argv;

  if (argv[2]) {
    console.log(argv[2]);
  } else {
    console.log('No argument');
  }
}
main();
