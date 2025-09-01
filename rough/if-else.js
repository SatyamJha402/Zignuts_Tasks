// if(2!=="3"){
//     console.log("!== executed");
// }
// if(2=="3"){
//     console.log("== executed");
// }
// if(2==="3"){
//     console.log("=== executed");
// }
// if(2!="2"){
//     console.log("!= executed");
// }

// if (60 > 500) console.log("test"), console.log("fail") // implicit scope


// if(5==5){
//     console.log("executed");
//     if(5==5){
//     console.log("again executed");
// }
// else{
//     console.log("again failed")
// }
// }

// else{
//     console.log("failed")
// }


//nullish coalescing operator (??)
// let val;
// val =  undefined?? null

// console.log(val);


// terniary operator
// const price = 9
// price >= 10 ? console.log("bought") : console.log("insufficient money");


// switch case
const month = 5
switch(month){
    case 1:
        console.log("jan");
        break
    case 2:
        console.log("feb");
        break
    default:
        console.log("other month");
        break
}