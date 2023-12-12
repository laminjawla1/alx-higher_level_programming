#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newKeys = [...new Set(Object.values(dict))];
const newDict = init(newKeys);

for (const d in dict) {
  newDict[dict[d]].push(d);
}
console.log(newDict);
function init (keys) {
  const dict = {};

  for (let i = 0; i < keys.length; i++) { dict[keys[i]] = []; }
  return dict;
}
