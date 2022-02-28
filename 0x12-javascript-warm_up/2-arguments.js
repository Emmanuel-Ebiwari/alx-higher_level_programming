#!/usr/bin/node
const { argv } = require('process');

const argLen = argv.length;
argLen > 2 ? argLen < 4 ? console.log('Argument found') : console.log('Arguments found') : console.log('No argument');
