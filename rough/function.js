// function addTwo(num1, num2){
//     // console.log(num1 + num2)
//     let res = num1 + num2
//     console.log("hello")
//     return res
// }

// res = addTwo(5, 7)
// const ans = addTwo(5, 7)
// console.log("result: ", ans)

// function loginUserMsg(name){
//     return `${name} just logged in`
// }

// console.log(loginUserMsg("hello"))

// const addTwo = (num1, num2) => {
//     return num1 + num2
// }

// const name = () => {
//     console.log("hello")
// }
// name();

//Implicit functions
// const addTwo = (num1, num2) => (num1 + num2)  //implicit function, don't need to explicitly return anything
// console.log(addTwo(1,2))

// const name = () => ({username: "hitesh"})
// console.log(name())



// // IIFE - immediately invoked function expression
// (function chai(){
//     console.log("DB Connected")
// })();
// (function chai2(){
//     console.log("DB disconnected")
// })();

// (() => {
//     console.log("DB connected again")
// })();

((name) => {
    console.log(`DB connected with ${name}`)
})("Satyam")