#!/usr/bin/node

const id = process.argv[2];
const url = 'http://swapi.co/api/films/' + id;
const rqst = require('request');
rqst.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (resp.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log(`Error code: ${resp.statusCode}`);
  }
});
