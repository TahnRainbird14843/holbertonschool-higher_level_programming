#!/usr/bin/node

const args = process.argv;

const int = parseInt(args[2]);

if (isNaN(int)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + int.toString());
}
