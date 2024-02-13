#!/usr/bin/node

const ParentSquare = require('./5-square');
module.exports = class Square extends ParentSquare {
	construtor (size) {
		super(size, size);
	}

	charPrint(c = "X") {
		for  (let idx = 0; idx < this.height; idx++) {
			console.log(c.repeat(this.width));
		}
	}
}
