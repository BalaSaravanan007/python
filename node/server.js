const http = require('http');

const server = http.createServer((req, res) => {
    if (req.url === '/'){
        res.end('Welcom to our Home Page!')
    }
    else if (req.url === '/about'){
        res.end('Here is our Short Story!')
    } else { res.end(`
        <h1>Oops...</h1>
        <p>We can't provide that page!!!</p>
        <a href = '/'>Back to Home Page</a>
        `)
    }
})

server.listen(5000)