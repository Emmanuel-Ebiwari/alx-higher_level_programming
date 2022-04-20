#!/usr/bin/node

const req = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

req(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  for (const characterId of JSON.parse(body).characters) {
    req(characterId, function (err, res, body) {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
