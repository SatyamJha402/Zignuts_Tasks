const prompt = require("prompt-sync")();
const input_str = prompt("Enter a String: ");
let sum = 0;

for(let i = 0; i < input_str.length; i++){
    const char = Number(input_str[i])
    if(!isNaN(char)){
        sum = sum + char;
    }
}

console.log("the sum is: ", sum);