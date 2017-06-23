#!/usr/bin/node
let size = process.argv[2];

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let output = '';
    for (let j = 0; j < size; j++) {
      output += 'X';
    }
    console.log(output);
  }
}
