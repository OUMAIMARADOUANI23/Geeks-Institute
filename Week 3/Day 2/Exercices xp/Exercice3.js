let userInput = prompt("Enter a number (10 or more):");
let number = Number(userInput);

while (isNaN(number) || number < 10) {
  alert(`You entered "${userInput}", which is not valid.`);
  userInput = prompt("Please enter a number greater than or equal to 10:");
  number = Number(userInput);
}

alert(`✅ Thank you! You entered ${number}, which is valid.`);
