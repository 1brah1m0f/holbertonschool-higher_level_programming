#!/usr/bin/node

let a = number(process.argv[2])
if (a === undefined) {
    console.log('Not a number')
} else {
    console.log('My number: ' + a)
}
