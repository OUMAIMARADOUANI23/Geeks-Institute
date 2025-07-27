const _ = require('lodash');
const { add, multiply } = require('./math');

console.log("Addition:", add(5, 3));
console.log("Multiplication:", multiply(5, 3));
console.log("Max:", _.max([1, 5, 3, 9]));
