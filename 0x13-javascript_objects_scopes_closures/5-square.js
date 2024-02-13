#!/usr/bin/node

const Rectangle = require('./4-retangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
