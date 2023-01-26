function revStr(str) {
    var name = "";
    for (var i = str.length - 1; i >= 0; i--) {
        name += str[i];
    }
    return name;
}
const input = prompt("Enter String Value : ");
console.log(revStr(input));