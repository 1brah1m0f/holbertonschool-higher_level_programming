#!/usr/bin/node

let a = process.argv[2]
if (a === String) {
    console.log('Not a number')
} else {
    console.log('My number:' + a)
}