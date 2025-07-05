let people = ["Greg", "Mary", "Devon", "James"];
people.shift();
console.log(people)
//--------------
const index =people.indexOf("James");
if (index==2){
people[index]="Jason";}
console.log(people)
//--------------
people.push("Oumaima") 
//--------------
const index1=people.indexOf("Mary");
console.log(index1);
//--------------
console.log(people)
//--------------
console.log(people.slice(1,-1))
//--------------
const index3=people.indexOf("Foo");
console.log(index3);
//--------------
const last=people[people.length -1]
console.log(last)
//--------------
for (let i=0;people.length>i;i++)
{
    if(people[i]!=="Devon"){
        console.log(people[i]);
        break;
    }
}
