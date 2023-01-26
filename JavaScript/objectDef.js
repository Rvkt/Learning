const person = {
    firstName: "John",
    lastName: "Doe",
    age: 50,
    eyeColor: "blue",
    id: 5566,
    fullName: function () {
        return this.firstName + " " + this.lastName;
    },
};

console.log(person.fullName());
