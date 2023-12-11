#!/usr/bin/node
function main () {
  const argv = process.argv;

  if (argv.length === 2) {
    console.log('No argument');
  } else {
    console.log(argv[2]);
  }
}
main();
