const { TestScheduler } = require("jest");
const fs = require('fs');

test('about.txt exists', () => {
    expect(fs.existsSync(__dirname + '/../static_content/about.txt')).toBe(true);
})

test('endpoints.js exists', () => {
    expect(fs.existsSync(__dirname + '/../static_content/endpoints.js')).toBe(true);
})