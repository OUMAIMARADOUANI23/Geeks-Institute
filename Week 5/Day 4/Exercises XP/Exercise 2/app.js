import { people } from "./data.js";
function calculateAverageAge(persons){
    const total=persons.reduce((sum,person)=>sum+person.age,0);
    return total/persons.length;
}
const avgAge =calculateAverageAge(people);
console.log("La liste:",people)
console.log("Average age:",avgAge.toFixed(2));