import Express from "express";

const app = Express();
const port = 1212;

app.get("/", (req, res) => {
    res.send("Hello World");
})

app.listen(port, () => {})