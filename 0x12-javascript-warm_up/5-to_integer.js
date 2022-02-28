#!/usr/bin/node
const { argv } = require('process');

isNaN(argv[2]) ? console.log('Not a number') : console.log(`My number: ${Math.floor(argv[2])}`);
