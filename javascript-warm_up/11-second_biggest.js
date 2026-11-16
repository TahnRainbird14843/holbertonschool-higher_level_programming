#!/usr/bin/node

const args = process.argv.slice(2);

const sorted = args.sort(function (a, b) { return parseInt(a) - parseInt(b); });

if (sorted.length < 2) {
  console.log(0);
} else {
  console.log(parseInt(sorted[sorted.length - 2]));
}
