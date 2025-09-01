const prompt = require("prompt-sync")();
let input = prompt("Enter a number: ");
input = Number(input)

function factorial(input) {
    if(input == 1 || input == 1){
        return 1
    }
    else{
        return (factorial(input-1) * input)
    }
}

const ans = factorial(input)
console.log(`the factorial of ${input} is ${ans}`);
