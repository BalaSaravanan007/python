console.log("Hello World"); // to print a function use console.log()
var x = 5; // creating a variable
var y = 2;
const z = x + y; // U can use all the arithmatic operations just like python
console.log(z); // this is a comment
console.log("the value of z is : " + z);
function My_func(a, b) {
  // creating a function
  return a * b;
}
a = My_func(5, 4);
console.log(a);

student = {
  // creating a object
  fname: "Bala",
  lname: "Saravanan",
  fullname: function () {
    // creating a function inside a object
    return this.fname + " " + this.lname;
  },
  course: {
    // creating a nested objects
    course1: "Python",
    course2: "JS",
  },
  level: "Beginer",
};
console.log(student);
x =
  student.fname +
  " is studying " +
  student.course.course1 + // accesing a nested object
  " as a " +
  student.level;
console.log(x);
console.log(student.fullname());

function Person(fname, lname, course, level) {
  // obj constructor: using this function u can create multiple objs
  this.fname = fname;
  this.lname = lname;
  this.course = course;
  this.level = level;
}

Student1 = new Person("Bala", "Saravanan", "Python, JS", "Beginer"); //creating multiple ojects Stu1 and Stu2 using the object constructor
Student2 = new Person("Dinesh", "Kumar", "C#, C++", "Beginer");

console.log(
  "My name is " +
    Student1.fname +
    " " +
    Student1.lname +
    "." +
    " I'm studying " +
    Student1.course +
    " as a " +
    Student1.level
);
Student2.MotherTongue = "Tamil"; // to add a property to a object

console.log(
  "His name is " +
    Student2.fname +
    " " +
    Student2.lname +
    "." +
    " He's studying " +
    Student2.course +
    " as a " +
    Student2.level +
    "." +
    " His mother tongue is " +
    Student2.MotherTongue
);
Person.prototype.MotherTongue = "Tamil"; // to add a property to obj constructor use .prototype
console.log(Student1.MotherTongue);

Student2.changecourse = function (cou) {
  // to add a method to a obj
  this.course = cou;
};
Student2.changecourse("JavaScript");
console.log(Student2.course);

Person.prototype.changelevel = function (lev) {
  // to add a method to a obj constructor use .prototype
  this.level = lev;
};

Student2.changelevel("Intermediate");
console.log(Student2.level);

var x = `it's all right we have "strength"`; // it is a template wchich can have both single and doubel qoutes
var y = x.length;
console.log(y);
console.log(x);
console.log(typeof x); //to say what is the type of x

if (new Date().getHours() < 18) {
  //if else conditions
  greetings = "Good day!";
  console.log(greetings);
} else if (new Date().getHours() >= 18) {
  greetings = "Had a great day?";
  console.log(greetings);
} else {
  greetings = "Have a great day ahead!";
}

var Number = 7;

if (Number % 2 == 0) {
  console.log("The number is even.");
} else {
  console.log("The Number is odd.");
}

var a = 3;
var b = 8;
var c = 9;

if (a >= b && a >= c) {
  console.log("a is the largest");
} else if (b >= a && b >= c) {
  console.log("b is the largest");
} else {
  console.log("c is the largest");
}

var year = 2024;

if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
  console.log("The given year is a Leap Year");
} else {
  console.log("The given year is not a Leap Year");
}

//electricity bill
var units = 320;
var bill = 0;

if (units <= 100) {
  bill = units * 0.5;
} else if (units >= 100 && units <= 200) {
  bill = 100 * 0.5 + (units - 100) * 0.75;
} else if (units >= 200 && units <= 300) {
  bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.2;
} else {
  bill = 100 * 0.5 + 100 * 0.75 + 100 * 1.2 + (units - 300) * 1.5;
}

console.log("Rupees", bill);

// function based simple problems

function sum(a, b) {
  return a + b;
}

console.log(sum(3, 4));

function CelciusToFarenheit(C) {
  return (C * 9) / 5 + 32;
}

console.log(CelciusToFarenheit(37));

function FarenheitToCelcius(F) {
  return ((F - 32) * 5) / 9;
}

console.log(FarenheitToCelcius(98.6));

function Factorial(n) {
  if (n == 0 || n == 1) {
    return 1;
  } else {
    return n * Factorial(n - 1);
  }
}

console.log(Factorial(5));

function ReverseString(str) {
  return str.split("").reverse().join("");
}

console.log(ReverseString("Bala"));

function isPalindrome(str) {
  let ReversedStr = str.split("").reverse().join("");
  if (str == ReversedStr) {
    return true;
  }
  return false;
}

console.log(isPalindrome("MALAYALAM"));

txt = "";
for (i = 0; i < 5; i++) {
  txt += "The number is " + i + "\n";
}
console.log(txt);

const arr = ["Apple", "Orange", "Mango"];
for (let x in arr) {
  console.log(arr[x]);
}

function ageCalculator(birthdate) {
  let today = new Date();
  let birthdateObj = new Date(birthdate);

  let age = today.getFullYear() - birthdateObj.getFullYear();
  let MonthDiff = today.getMonth() - birthdateObj.getMonth();
  let dayDiff = today.getDate() - birthdateObj.getDate();

  if (MonthDiff < 0 || (MonthDiff == 0 && dayDiff < 0)) {
    age--;
  }
  return age;
}

let birthdate = "06-04-2007";
console.log(ageCalculator(birthdate));

// loops based problems

function SumOfNaturalNumbers(n) {
  let sum = 0;
  for (i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}

console.log(SumOfNaturalNumbers(100));

function ReverseNumber(n) {
  let revNum = 0;
  while (n > 0) {
    let digit = n % 10;
    revNum = revNum * 10 + digit;
    n = Math.floor(n / 10); //use Math.floor() to round of the number
  }
  return revNum;
}

console.log(ReverseNumber(13));

function isPrime(n) {
  for (i = 2; i <= Math.sqrt(n); i++) {
    if (n % i == 0) {
      return "Not Prime";
    } else {
      return "Prime";
    }
  }
}

console.log(isPrime(12));

function MultiplicationTable(n) {
  for (i = 1; i <= 10; i++) {
    console.log(n, "*", i, "=", n * i);
  }
}

MultiplicationTable(8);

function ArrSum(Arr) {
  sum = 0;
  for (i = 0; i < Arr.length; i++) {
    sum += Arr[i];
  }
  return sum;
}
console.log(ArrSum([1, 2, 3, 4]));

function Stars(n) {
  for (let i = 1; i <= n; i++) {
    let stars = " ";
    for (let j = 1; j <= i; j++) {
      stars += " * ";
    }
    console.log(stars);
  }
}

Stars(5);

function inStars(n) {
  for (let i = n; i >= 1; i--) {
    let stars = " ";
    for (let j = 1; j <= i; j++) {
      stars += " * ";
    }
    console.log(stars);
  }
}

inStars(4);

function Diamond(n) {
  for (i = 1; i <= n; i++) {
    let spaces = " ".repeat(n - i);
    let stars = " *".repeat(i);
    console.log(spaces + stars);
  }

  for (i = 1; i <= n; i++) {
    let spaces = " ".repeat(i);
    let stars = " *".repeat(n - i);
    console.log(spaces + stars);
  }
}

Diamond(5);

// function hollowSquare(n) {
//   for (i = 1; i <= n; i++) {
//     let stars = "";
//     for (j = 1; j <= i; j++) {
//       stars += "*  ";
//       console.log(stars);
//     }

//     for (i = 1; i <= n; i++) {
//       // let spaces = " ".repeat(i);
//       let stars = " *".repeat(n - i);
//       console.log(stars);
//     }
//   }
// }
// hollowSquare(4);
