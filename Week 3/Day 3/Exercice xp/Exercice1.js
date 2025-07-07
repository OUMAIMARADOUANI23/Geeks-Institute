
function displayNumbersDivisible(divisor=23)
{
    let sum=0
    for(let i=0;i<501;i++){
         if(i%divisor===0)
    {
        console.log("Outcome:",i)
        sum+=i
    }
    }
   console.log("Sum:",sum)
}
displayNumbersDivisible();

