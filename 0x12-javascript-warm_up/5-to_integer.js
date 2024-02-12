#!/usr/bin/node
const arg1 = process.argv[2];
const intNum = parseInt(arg1);

if (intNum) {
  console.log(`My number: ${intNum}`);
} else {
  console.log('Not a number');
}
