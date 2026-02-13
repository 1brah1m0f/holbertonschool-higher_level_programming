#!/usr/bin/node

let a = process.argv[2];
if (isNaN(a) === String) {
    console.log('Not a number');
} else {
    console.log('My number: ' + a);
}