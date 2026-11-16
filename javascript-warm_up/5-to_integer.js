#!/usr/bin/node


let args = process.argv;

let int = parseInt(args[2]);

if (int == NaN) {
  console.log('Not a number');
} else {
  console.log('My number: ' + int.toString());
};
