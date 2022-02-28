#!/usr/bin/node
const { argv } = require('process');

let argLen = argv.length

argLen > 2 ?  argLen < 4 ? console.log('Argument found') : console.log('Arguments found') : console.log('No argument');
