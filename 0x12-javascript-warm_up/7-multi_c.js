#!/usr/bin/node
const str = 'C is fun';
const nTimes = parseInt(process.argv[2]);

for (let i = 0; i < nTimes; i++) {
  console.log(str);
}
