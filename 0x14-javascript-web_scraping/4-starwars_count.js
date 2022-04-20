#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req(url, function (err, res, body) {
  if (err) console.log(err);
  const data = JSON.parse(body);
  let count = 0;
  for (const result of data.results) {
    for (const character of result.characters) {
      if (character.includes(18)) {
        count++;
      }
    }
  }
  console.log(count);
});
