#!/usr/bin/node
const x = Number(process.argv[2]);
let x1 = x;
let i = 0;
let a = '';
while (x1 > 0) {
  a = a + "X";
  x1--;
}
if (isNaN(x)) {
  console.log('Missing size')
} else {
  while (i < x) {
    console.log(a);
    i++;
  }
}
