#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((typeof w === 'number' && typeof h === 'number') && (w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
