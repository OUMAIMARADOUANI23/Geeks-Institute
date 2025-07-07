const stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
};

const prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
};

const shoppingList = ["banana", "orange", "apple"];

function myBill() {
  let total = 0;

  for (let item of shoppingList) {
    if (item in stock && stock[item] > 0) {
      total += prices[item];    
      stock[item]--;            
    }
  }

  return total;
}

console.log("Total bill:", myBill());
console.log("Updated stock:", stock);
