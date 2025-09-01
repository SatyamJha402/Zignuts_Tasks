const myArr = [0, 1, 2, 3, 4, 5, true, "name"]
// console.log(myArr[5])

const newArr1 = new Array(2,4,6,8);
// console.log(newArr1)

// myArr.push(7)
// console.log(myArr)

// myArr.pop()
// console.log(myArr)

// myArr.unshift(9)
// console.log(myArr)
// myArr.shift()
// console.log(myArr)

// console.log(myArr.includes(5))
// console.log(myArr.indexOf(2))

// const newArr = myArr.join()
// console.log(newArr)
// console.log(typeof newArr)

// console.log("A", myArr)

// const myn1 = myArr.slice(1,3)
// console.log("B", myn1)
// console.log(myArr)
// const myn2 = myArr.splice(1,3)
// console.log("C", myn2)
// console.log(myArr)


// const arr1 = myArr.push(newArr1)
// const arr2 = myArr.concat(newArr1)
// // console.log(arr1)
// console.log(arr2)

// const arr1 = [...myArr, ...newArr1]
// console.log(arr1)

const another_arr = [1, 2, 3, [4, 5, [6, 7], 8], 9]
const real_Arr = another_arr.flat(Infinity)
console.log(real_Arr)

console.log(Array.isArray("Name"))
console.log(Array.from("Name"))
console.log(Array.from({name: "Satyam"}))  //doesn't work

let new_arr = [1, 2]
let score = 5
let str = "hello"

console.log(Array.of(str, score, new_arr))

const my_array = [myArr, newArr1]
console.log("array", my_array)
