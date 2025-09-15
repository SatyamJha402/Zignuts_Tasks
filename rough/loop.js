// for(let i = 0; i <5; i++){
//     for(let j = 0; j <= i; j++){
//         process.stdout.write("*")
//     }
//     process.stdout.write("\n");
// }

// let score = 1
// do {
//     console.log(score)
//     score++
// } while(score <= 10);

// let score1 = 1
// while(score1<=10){
//     console.log(score1)
//     score++
// }


// const fruits = ["apple", "banana", "cherry"]
// for (const item of fruits){
//     console.log(item);
// }

// const fruits = ["apple", "banana", "cherry"]
// for (const [index, items] of fruits.entries()){
//     console.log(items);
// }


// const fruits = ["apple", "banana", "cherry"]
// for (const index in fruits){
//     console.log(fruits[index]);
// }


// const detail = {name: "satyam",
//                 age: 22,
//                 email: "sat@gmail.com"
// }
// for (const item in detail){
//     console.log(item, detail[item])
// }


// const num = [1, 2, 3, 4]
// const newNum = num.map((item) => item*2)
// console.log(newNum);



const coding = ["js", "ruby", "java", "python"]

// const values = coding.forEach((item) => {
//     // console.log(item)
//     return item
// })   // for Each - doesn't return anything


const myNum = [1, 2, 3, 4, 5, 6]
// const newNum = myNum.filter((num) => num>4)
// const newNum = myNum.filter((num) => {
//     return num > 4
// })
// console.log(newNum)


// const nums = myNum.map((num) => num * 10).map((num) => num+1).filter((num) => num >= 40)
// console.log(nums);


// const arr = [1, 2, 3, 4]
// const initvalue = 5
// const newArr = arr.reduce(
//     function(acc, currval) {
//         console.log(acc, currval)
//         return (acc + currval)}
//     ,initvalue)
// console.log(newArr)

// const full = xyz("mr.", "spongebob")
// function xyz(...params) {
//     return params.join(" ")
// }
// console.log(full);

// let name = {
//     first : "satyam",
//     last : "jha",
//     fullname:{
//         // first : "some",
//         // last : "name",
//         printfullname : function(){
//             const innerf = () => {
//                 console.log(this.first + this.last);
//             }
//             innerf();
//     }
// }   
// }
// name.fullname.printfullname();

// console.log(isNaN("HELLO"));

// var emp = {
//     company:"some",
//     name:"another"
// }

// emp.salary = 1000

// delete emp.company
// delete emp.name
// delete emp.salary

// console.log(emp);

// function x(a){
//     a();
//     console.log("x");
// };

// x(function y(){
//     console.log("y");
// });

var hello = setTimeout(() => {
    console.log("hello");
}, 5000);

hello()