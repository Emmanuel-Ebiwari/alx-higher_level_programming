#!/usr/bin/node

const req = require('request');
const id = process.argv[2];

req(`https://swapi-api.hbtn.io/api/films/${id}`, function (err, res, body) {
  if (err) console.error(err);
  const data = JSON.parse(body);
  console.log(data.title);
});
