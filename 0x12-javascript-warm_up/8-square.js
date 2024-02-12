#!/usr/bin/node
const size = parseInt(process.argv[2]);
const strFull = 'X'.repeat(size);

if (size) {
  for (let idx = 0; idx < size; idx++) {
    console.log(strFull);
  }
} else {
  console.log('Missing size');
}
