document.addEventListener("DOMContentLoaded",()=>{
    const button = document.getElementById("button");
    const nameEl = document.getElementById("name");
    const heightEl = document.getElementById("height");
    const genderEl = document.getElementById("gender");
    const birthYearEl = document.getElementById("birth-year");
    const homeWorldEl = document.getElementById("home-world");

    button.addEventListener("click",async()=>{
        nameEl.innerHTML = `<i class="fa fa-spinner fa-spin"></i> Loading...`;
        heightEl.innerHTML = "";
        genderEl.innerHTML = "";
        birthYearEl.innerHTML = "";
        homeWorldEl.innerHTML = "";
    const randomId = Math.floor(Math.random() * 83) + 1;
    
    try{

    const response=await fetch(`https://www.swapi.tech/api/people/${randomId}`);
    const data=await response.json();
    const character=data.result.properties;

    const homeworldResponse = await fetch(character.homeworld);
    const homeworldData = await homeworldResponse.json();
    const homeworldName = homeworldData.result.properties.name;

    nameEl.textContent=`Name:${character.name}`;
    heightEl.textContent=`Height:${character.height} cm`;
    genderEl.textContent=`Gender:${character.gender}`;
    birthYearEl.textContent=`Birth Year:${character.birth_year}`;
    homeWorldEl.textContent=`Home World:${homeworldName}`;
    }

    catch (error) {
    nameEl.textContent = "Error fetching character.";
    console.error("Erreur :", error);
    }
});
});