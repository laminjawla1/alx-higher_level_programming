#!/usr/bin/node
/**
 * Computes the number of tasks completed by user id..
 */

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const result = {};
    todos.forEach(todo => {
      if (todo.completed === true) {
	if (result[todo.userId] === undefined)
	  result[todo.userId] = 1;
	else
	  result[todo.userId]++;
      }
    });
    console.log(result);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
