#!/usr/bin/node

function factorial (n) {
  if (n === 1) {
    return n;
  }

  return n * factorial(n - 1);
}

let arg = parseInt(process.argv[2]);

if (isNaN(arg)) {
  arg = 1;
} else if (arg > 0) {
  console.log(factorial(arg));
}
