const { TestScheduler } = require("jest");
const fs = require('fs');

test('about.txt exists', () => {
    expect(fs.existsSync(__dirname + '/../static_content/about.txt')).toBe(true);
})

test('endpoints.json exists', () => {
    expect(fs.existsSync(__dirname + '/../static_content/endpoints.json')).toBe(true);
})