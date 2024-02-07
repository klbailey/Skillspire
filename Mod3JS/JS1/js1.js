console.log('Javascript Assignment 1');

console.log("Hello World");
console.log("Kathy, green");
// SUM
a = 1;
b = 2;
c = a + b;
console.log(c);
// String of first and last name
let firstname = 'Kathy';
let lastname = 'Bailey Hines';
console.log(firstname + " " + lastname);
// Create a for loop that prints all values from 1-10
for (let i = 1; i <= 10; i++) {
    console.log(i);
}
// Create a for loop that prints the word "Skillspire" 5 times
for (i = 1; i < 6; i++) {
    console.log("Skillspire");
}
// Create a for loop that multiplies all values from 1-10 
// by 2 and print these values out to the console. The output should look like: 2 4 6 8 10 12 14 16 18 20
for (i = 1; i < 11; i++) {
    x = i * 2;
    console.log(x);
}
// Create a for loop that prints all EVEN values from 1-20
for (i = 2; i < 21; i += 2) {
    console.log(i);
}
// Create a for loop that prints all ODD values from 1-20
for (i = 1; i < 21; i++) {
    if (i % 2 != 0) {
        console.log(i);
    }
}
// Create a for loop that starts at 1 and ends at 10. 
// If a value is even have the console print out “FIZZ”. If the value is odd have the console print out “BUZZ”.
for (i = 1; i <= 10; i++) {
    if (i % 2 != 0) {
        console.log('BUZZ');
    }
    else {
        console.log('FIZZ');
    }
}
