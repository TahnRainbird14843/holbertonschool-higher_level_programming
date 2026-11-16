#!/usr/bin/node


let arg = parseInt(process.argv[2]);

if (isNaN(arg)) {
    console.log("Missing size");
}
else if (arg > 0) {
    str = ""
    for (let i = 0; i < arg; i++) {
        str += "X";
    }
    for (i = 0; i < arg; i++) {
        console.log(str)
    }
}