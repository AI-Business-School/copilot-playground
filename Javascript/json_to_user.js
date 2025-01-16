
// Exercise: JSON to User Class Converter
// Practice class and JSON manipulation with Github Copilot

class User {
    constructor(name, email, password) {
        this.name = name;
        this.email = email;
        this.password = password;
    }
}

const user = {
    name: "John Doe",
    email: "johndoe@gmail.com",
    password: "password123"
};

// TODO: Write a function that takes in a JSON and returns a User class
function createUser(json) {
    const { name, email, password } = JSON.parse(json);
    return new User(name, email, password);
}

// TODO: Write a function that takes in a User class and returns a JSON
function jsonifyUser(user) {
    return JSON.stringify(user);
}

module.exports = {
    User,
    createUser,
    jsonifyUser
};