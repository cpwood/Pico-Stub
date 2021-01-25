/*
* Load the single-quoted JSON from Python's repr() function, prettify
* and save as conventional double-quoted JSON.
*/
var fs = require('fs');

var content = fs.readFileSync('../stub/micropython-rp2-1_13-290/modules.json', 'utf8');
var obj = (0, eval)('(' + content + ')');
fs.writeFileSync('../stub/micropython-rp2-1_13-290/modules.json', JSON.stringify(obj, null, 4));