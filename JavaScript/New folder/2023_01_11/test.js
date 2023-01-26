// GIVING THE COMMAND TO THE CONSOLE TO FETCH MY JSON BONE
fetch('https://dummyjson.com/products')
.then(Response => Response.json()) // parsing // ()=>{} _Ar
.then((Response)=>{
// Product names
const name = Response.products.map(
// Below function is for iteration
function(index) {
console.log(index.id)
console.log(index.title)
return index.title
}
)
});