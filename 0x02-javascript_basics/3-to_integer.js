#!/usr/bin/node
let input = process.argv;
let argument = input[2];

if (isNaN(input)) {
  console.log('Not a number');
} else {
  console.log('My number:', input);
}
