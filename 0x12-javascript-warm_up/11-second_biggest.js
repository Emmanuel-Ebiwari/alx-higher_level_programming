#!/usr/bin/node
const { argv } = require('process');

if (argv.length < 4) {
  console.log(0);
} else {
  argv.sort((a, b) => a - b);
  console.log(argv);
  console.log(argv[argv.length - 2]);
}
