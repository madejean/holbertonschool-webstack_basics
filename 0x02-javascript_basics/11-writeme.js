#!/usr/bin/node
var fs = require('fs');
file = process.argv[2];
str = process.argv[3];

fs.writeFile(file, str, 'utf8', function(err) {
    if(err) {
        return console.log(err);
    }
});
