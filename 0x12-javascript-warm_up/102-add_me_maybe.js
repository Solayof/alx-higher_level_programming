#!/usr/bin/node

exports.addmeMaybe = function (number, theFunction) {
	const num = number++;
	theFunction(num);
};
