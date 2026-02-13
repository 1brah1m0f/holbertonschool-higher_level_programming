#!/usr/bin/node
let max = Number(process.argv[2]);
let second = 0;

for (let i = 3; i < process.argv.length; i++) {
  const num = Number(process.argv[i]);
  if (num > max) {
    second = max;
    max = num;
  } else if (num > second) {
    second = num;
  }
}

console.log(second);
