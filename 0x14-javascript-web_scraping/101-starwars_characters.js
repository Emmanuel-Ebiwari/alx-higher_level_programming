#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

req(url, async function (err, res, body) {
  if (err) {
    console.log(err);
  }
  for (const characterId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      req(characterId, function (err, res, body) {
        if (err) {
          reject(err);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
