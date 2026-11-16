#!/usr/bin/node

let args = process.argv.slice(2);

let sorted = args.sort(function(a, b){return parseInt(a) - parseInt(b)});

if (sorted.length < 2) {
    console.log(0);
} else {
    console.log(parseInt(sorted[sorted.length - 2]));
}