const prompt = require("prompt-sync")();

function hotelCost(nights) {
  return nights * 140;
}

function planeRideCost(destination) {
  destination = destination.toLowerCase();
  if (destination === "london") return 183;
  if (destination === "paris") return 220;
  return 300;
}

function rentalCarCost(days) {
  let cost = days * 40;
  return days > 10 ? cost * 0.95 : cost;
}

function getValidNumber(question) {
  let value;
  do {
    value = parseInt(prompt(question));
  } while (isNaN(value) || value < 0);
  return value;
}

function getValidText(question) {
  let text;
  do {
    text = prompt(question);
  } while (!text || !isNaN(text));
  return text;
}

function totalVacationCost() {
  const nights = getValidNumber("How many nights at the hotel? ");
  const destination = getValidText("What is your destination? ");
  const days = getValidNumber("How many days do you want to rent a car? ");

  const hotel = hotelCost(nights);
  const plane = planeRideCost(destination);
  const car = rentalCarCost(days);
  const total = hotel + plane + car;

  console.log(`Hotel: $${hotel}, Plane: $${plane}, Car: $${car}`);
  console.log(`Total vacation cost: $${total}`);
  return total;
}

totalVacationCost();
