#!/usr/bin/node
let id = process.argv[2];
let url = "http://swapi/api/films/" + id;
rqst = reqiure('request');
rqst.get(url, (err,  resp, body) => {
    if (err) {
        console.log(err);
    } else if (resp.statusCode === 200) {
        body = JSON.parse(body);
        console.log(body["title"]);
    } else {
        console.log(`Error code: ${resp.statusCode}`);
    }
});
