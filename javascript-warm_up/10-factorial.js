#!/usr/bin/node
const a = Number(process.argv[2]);
const i = 1;
let f = 1;
function fact (i) {
  if (isNaN(a)) {
    console.log('1');
  } else {
    while (i <= a) {
      f = f * i;
      i++;
    }
    console.log(f);
  }
}
fact(i);
