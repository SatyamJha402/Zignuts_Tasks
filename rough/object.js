// Object.create - singelton

//object literal
const obj1 = {
    name : {
        firstname : "Satyam",
        lastname : "Jha"
    },
    age : 22
}

const obj2 = {
    age: 23,
    email: "sat@gmail.com"
}

// console.log(obj1.name.firstname)

// const obj3 = {obj1 , obj2}
// console.log(obj3)

// const obj3 = Object.assign({}, obj1, obj2)
// const obj4 = {...obj1, ...obj2}
// console.log(obj4)


// console.log(Object.keys(obj1))
// console.log(Object.values(obj1))
// console.log(Object.entries(obj1))

const {email : id} = obj2
// console.log(email)
console.log("id", id)