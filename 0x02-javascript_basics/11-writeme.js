#!/usr/bin/node
let fs = require('fs');
let file = process.argv[2];
let str = process.argv[3];

fs.writeFile(file, str, 'utf8', function (err) {
  if (err) {
    return console.log(err);
  }
});
