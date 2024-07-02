// console.log(__dirname)
// console.log(__filename)
// console.log(process)
// console.log(module)

// setInterval(() => {
//     console.log("Hello, World!")
// }, 1000)

// setTimeout(() => {
//     console.log("This programme runs after 2 seconds!")
// }, 2000)

// const names = require("./names");
// const Greetings = require("./Greetings");
// console.log("Hello");

// Greetings("Bala");
// Greetings(names.john);
// Greetings(names.fred);

// function stepOne(callback) {
//   setTimeout(function () {
//     console.log("Step One completed");
//     callback();
//   }, 1000);
// }

// function stepTwo() {
//   console.log("Step Two completed");
// }

// // Usage
// stepOne(() => {
//   stepTwo();
// });

// function calculate(num1, num2, operation, callbak) {
//   let result;
//   switch (operation) {
//     case "add":
//       result = num1 + num2;
//       break;
//     case "subtract":
//       result = num1 - num2;
//       break;
//     case "multiply":
//       result = num1 * num2;
//       break;
//     case "divide":
//       result = num1 / num2;
//       break;
//     default:
//       result = "Invalid operation";
//   }
//   callbak(result);
// }

// // Callback function to handle the result
// function handleResult(result) {
//   console.log("Result:", result);
// }

// // Usage
// calculate(10, 5, "add", handleResult); // Result: 15
// calculate(10, 5, "subtract", handleResult); // Result: 5
// calculate(10, 5, "multiply", handleResult); // Result: 50
// calculate(10, 5, "divide", handleResult); // Result: 2
// calculate(10, 5, "modulo", handleResult);

// function isEven(num, callback) {
//   let result;
//   if (num % 2 === 0) {
//     result = "This is Even";
//   } else {
//     result = "This is Odd";
//   }
//   callback(result);
// }

// function showresult(result) {
//   console.log(result);
// }

// isEven(2, showresult);

// function Hello(callback) {
//   console.log("Hello!");
//   callback();
// }

// function GoodBye() {
//   console.log("Good Bye!");
// }

// Hello(GoodBye);

// function info(arr, callback) {
//   for (let i = 0; i < arr.length; i++) {
//     callback(arr[i], i);
//   }
// }

// function handleItems(item, index) {
//   console.log(`Item at index ${index}:`, item);
// }

// fruits = ["Apple", "Banana", "Orange"];
// info(fruits, handleItems);

// function fetchData(callback) {
//   setTimeout(() => {
//     let data = { fname: "Bala", lname: "Saravanan", Course: "Back end" };
//     callback(data);
//   }, 1000);
// }

// function handleData(data) {
//   console.log(data);
// }

// fetchData(handleData);

// function Eventlistener(eventType, callback) {
//   setTimeout(() => {
//     let event = { Event: eventType, TimeStamp: new Date() };
//     callback(event);
//   }, 2000);
// }

// function EventHandler(event) {
//   console.log(event);
// }

// Eventlistener("Click", EventHandler);

// let promise = new Promise((resolve, reject) => {
//   let Success = true;
//   if (Success) {
//     resolve("The operation is Successfull");
//   } else {
//     reject("Operation Failed");
//   }
// });

// promise
//   .then(function (result) {
//     console.log(result);
//   })
//   .catch((error) => {
//     console.error(error);
//   });

// console.log("first");

// let fetchData = function () {
//   return new Promise((resolve, reject) => {
//     setTimeout(() => {
//       let Data = { fname: "Bala", lname: "Saravanan" };
//       if (Data) {
//         resolve(Data);
//       } else {
//         reject(error);
//       }
//     }, 2000);
//   });
// };

// fetchData()
//   .then((Data) => {
//     console.log("Here is the Data:", Data);
//   })

//   .catch((error) => {
//     console.error("An error occured", error);
//   });

// console.log("Second");

// function delay(ms) {
//   return new Promise((resolve) => {
//     setTimeout(resolve, ms);
//   });
// }

// delay(1000)
//   .then(() => {
//     console.log("1 Second Passed");
//     return delay(2000);
//   })
//   .then(() => {
//     console.log("3 Seconds Passed");
//   });

// function fetchData1() {
//   return new Promise((resolve) => {
//     setTimeout(() => {
//       Data1 = { fname: "Bala", lname: "Saravanan" };
//       resolve(`Here is the Data1, ${Data1}`);
//     }, 1000);
//   });
// }

// function fetchData2() {
//   return new Promise((resolve) => {
//     setTimeout(() => {
//       Data2 = { fname: "Dinesh", lname: "Kumar" };
//       resolve(`Here is the Data2, ${Data2}`);
//     }, 2000);
//   });
// }

// Promise.all([fetchData1(), fetchData2()])
//   .then((result) => {
//     console.log(result);
//   })
//   .catch((error) => {
//     console.error(error);
//   });
