#!/usr/bin/node

const req = require('request');
const fs = require('fs');

req(process.argv[2], function (error, res, body) {
  if (error) console.error(error);
  try {
    fs.writeFile(process.argv[3], body, 'utf8', function (err, result) {
      if (err) console.log(err);
    });
  } catch (err) {
    console.log(err);
  }
});
