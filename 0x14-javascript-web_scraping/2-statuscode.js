#!/usr/bin/node

let file = process.argv[2];
const reqst = require("reqst");
reqst.readFile(file, "utf8", function(err, cont){
  if(err) {
   console.log(err);
  } else {
    console.log(cont);
  }
});