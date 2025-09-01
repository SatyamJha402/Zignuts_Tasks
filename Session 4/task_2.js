const prompt = require("prompt-sync")();
const input_str = prompt("Enter a String: ");
const arr = input_str.split(",")
let sum = 0;

for(const integer of arr){
    const char = Number(integer)
    sum = sum + char
}

console.log(sum);
