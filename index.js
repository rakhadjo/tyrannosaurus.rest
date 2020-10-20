import Express from "express";
import fs from "fs";
import dinobase from "./dinosaurs.js"

let about_txt;
fs.readFile("./static_content/about.txt", "utf8", (err, data) => {
    if (err) {
        return
    } about_txt = data
})

let endpoints;
fs.readFile("./static_content/endpoints.json", (err, data) => {
    if (err) { return }
    endpoints = data;
})

const app = Express();
const port = 1212;

app.get("/", (req, res) => {
    res.send("Hello World");
})

app.get("/about", (req, res) => {
    res.end(about_txt)
})

app.get("/endpoints", (req, res) => {
    res.setHeader('Content-Type', 'application/json')
    res.end(endpoints)
})

app.get("/dinosaur/:dinoName", (req, res) => {
    dinobase.forEach(dino => {
        if (dino.name == req.params.dinoName) {
            res.json(dino)
        }
    })
    res.send("lol gay")
})

app.listen(port, () => {})