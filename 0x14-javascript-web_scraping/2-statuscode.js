#!/usr/bin/node

const url = process.argv[2];
const reqs = require('request');
reqs.get(url, (err, resp) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${resp.statusCode}`);
  }
});
