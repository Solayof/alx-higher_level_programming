#!/usr/bin/node

const id = process.argv[2];
const url = 'http://swapi/api/films/' + id;
const rqst = reqiure('request');
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
