#!/usr/bin/node
function main () {
  const dict = require('./101-data.js').dict;

  const newKeys = getUniqueKeys(Object.values(dict));
  const newDict = init(newKeys);

  for (const d in dict) {
    newDict[dict[d]].push(d);
  }
  console.log(newDict);
}
function getUniqueKeys (list) {
  const newList = [];

  for (let i = 0; i < list.length; i++) {
    if (newList.indexOf(list[i]) === -1) {
      newList.push(list[i]);
    }
  }
  return newList;
}
function init (keys) {
  const dict = {};

  for (let i = 0; i < keys.length; i++) { dict[keys[i]] = []; }
  return dict;
}
main();
