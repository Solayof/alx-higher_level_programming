#!/usr/bin/node
const xNum = parseInt(process.argv[2]);
const langs = 'C is fun';

if (xNum) {
  for (let idx = 0; idx < xNum; idx++) {
    console.log(langs);
  }
} else {
  console.log('Missing number of occurance');
}
