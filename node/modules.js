const { log } = require('console');
const os = require('os');

// let user = os.userInfo();
// console.log(user);

// let time = os.uptime();   // uptime : how long the system been running after a restart or reboot
// console.log(`the uptime of the computer is ${time} seconds`);

// const currentOS = {
//     'name' : os.type(),
//     'release': os.release(),
//     'total_memory': os.totalmem()+' bytes', 
//     'free_memory': os.freemem()+' bytes'
// }

// console.log(currentOS)

// console.log(os.networkInterfaces())
// console.log(os.platform())

// const path = require("path");
// console.log(path.sep)


////synchronous way 
const fs = require('fs');
// let read = fs.readFileSync('./test.txt', 'utf-8');
// fs.writeFileSync(
//     './result.txt', 
//     `I have read the file ${read} and here is what i have weitten!`,
//     {flag :'a'}
// );

//// Asynchronous way 

fs.readFile('./test.txt', 'utf-8', (err, result) => {
    if (err){
        console.log(err)
    } else {
        console.log(result)
    }
    const test = result
    fs.readFile('./test2.txt', 'utf-8', (err, result) => {
        if (err){
            console.log(err)
        } else {
            console.log(result)
        }
        const test2 = result
        fs.writeFile(
            './result.txt',
            `this is the result ${test}, ${test2}`,
            (err, result) => {
                if (err) {
                    console.log(err)
                } 
            }
        )
    })
})