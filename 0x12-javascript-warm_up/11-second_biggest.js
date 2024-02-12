#!/usr/bin/node
 const numArray = process.argv.slice(2, process.argv.length).sort((a, b) => a - b);

if (process.argv.length<= 3) {
	console.log(0);
} else {
	console.log(numArray[numArray.length - 2]);
}
