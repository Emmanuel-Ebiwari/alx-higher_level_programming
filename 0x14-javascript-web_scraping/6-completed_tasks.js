#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req(url, function (err, res, body) {
  if (err) console.log(err);
  const completed = {};
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (completed[task.userId]) {
        completed[task.userId]++;
      } else {
        completed[task.userId] = 1;
      }
    }
  }
  console.log(completed);
});
