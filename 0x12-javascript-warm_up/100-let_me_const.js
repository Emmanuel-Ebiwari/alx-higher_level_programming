#!/usr/bin/node

let myVar = require('./100-main').myVar;
myVar = 333;
module.exports = { myVar };
