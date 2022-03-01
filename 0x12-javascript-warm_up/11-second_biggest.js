#!/usr/bin/node
const { argv } = require('process');

// function add (a, b) {
//  console.log(Number(a) + Number(b));
// }

if (argv.length < 4) {
  console.log(0);
} else {
  argv.sort();
  console.log(argv[argv.length - 2]);
}
