#!/usr/bin/node

const count = process.argv.length - 2;
const arg = process.argv[2]

if (count === 0 ) {
    console.log('No argument')
} else {
    console.log(arg)
}