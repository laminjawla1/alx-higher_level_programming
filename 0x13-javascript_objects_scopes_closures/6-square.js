#!/usr/bin/node

const SquareOne = require('./5-square');

module.exports = class Square extends SquareOne {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += c;
      }
      console.log(str);
    }
  }
};
