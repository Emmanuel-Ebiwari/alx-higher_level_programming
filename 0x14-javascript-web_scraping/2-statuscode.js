#!/usr/bin/node

const req = require('request');

req(process.argv[2], function (error, res) {
  if (error) {
    console.error(error);
  }
  console.log('code:', res.statusCode);
});
