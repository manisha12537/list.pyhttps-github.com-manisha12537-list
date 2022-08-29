var get_input=require("readline-sync")
var a=get_input.questionInt("enter number")
var b=get_input.questionInt("enter number")
var c=get_input.questionInt("enter number")
var data=(a>b && a>c)?(b>c?b:c):(b>a && b>c)?(c>a?c:a):(c>a && c>b)?(a>b?a:b):'same';
console.log(data)


// var data=(a>b && a>c)?a:(b>a && b>c)?b:(c>a && c>b)?c:"same"
// console.log(data)



// let x = 10;
// let y = (x++, x + 1);
// console.log(x, y);



// const numbers = [1, 3, 5, 7];

// function addNumbers(a, b, c, d) {
//   return a + b + c + d;
// }

// console.log(addNumbers(...numbers));

// // The invocation above will return:
// 16


// var arr=[1,2,4]
// var arr_2=[4,7,...arr]
// console.log(...arr)
// output: [4,7,1,2,4]


// var obj_1={a:2,b:6,c:8}
// var obj_2={...obj_1,z:6,y:9}
// console.log(...obj_1)


// function my_fun(a,b,...c){
// 	console.log(a+b+c)
// }
// my_fun(3,4,9,6,8,9)
// // output: [9,6]



// var a=require("readline-sync")
// var b=a.questionInt("enter anything")
// switch(b){
//     case 1:
//         console.log("one")
//         break
//     case 2:
//         console.log("two")
//         break
//     case 3:
//         console.log("three")
//         break
//     case 4:
//         console.log("four")
//         break
//     case 5:
//         console.log("five")
//         break
//     default:
//         console.log("error")
// }