const http = require("http");
const fs = require("fs");

const html = fs.readFileSync("index.html");
const style = fs.readFileSync("style.css");
const tomato = fs.readFileSync("happy-tomato.png");
const bell = fs.readFileSync("bell.png");

const server = http.createServer(function (req, res) {
    if (req.url === "/style.css") {
        res.writeHead(200, {"Content-Type": "text/css"});
        res.write(style);
    } else if (req.url === "/happy-tomato.png") {
        res.writeHead(200, {"Content-Type": "image/png"});
        res.write(tomato);
    } else if (req.url === "/bell.png") {
        res.writeHead(200, {"Content-Type": "image/png"});
        res.write(bell);
    } else {
        res.writeHead(200, { "Content-Type": "text/html" }); 
        res.write(html);
    }
    res.end();
});

server.listen(5000);