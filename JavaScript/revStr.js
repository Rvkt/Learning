var string  = prompt("Please enter a string:");
var strLen = string.length;
        
// console.log(string)
revStr = '';
for(var i = strLen-1; i>=0; i--){
    revStr += string[i];
}

console.log(`${string} reverse is ${revStr}`)