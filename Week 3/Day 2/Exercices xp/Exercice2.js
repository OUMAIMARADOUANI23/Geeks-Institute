const colors=["Noir","Blanc","Rouge","Marron","Jaune"]
const suffixes = ["premier", "deuxième", "troisième", "quatrième", "cinquième"];
for (let i=0;colors.length>i;i++)
{
    console.log(`Mon ${suffixes[i]} choix est ${colors[i]}`);
}