#!/usr/bin/node

const file = process.argv[2];
const str = process.argv[3];
const fs = require('fs');
fs.writeFile(file, str, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
