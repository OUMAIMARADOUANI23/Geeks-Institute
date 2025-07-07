const containerDiv = document.getElementById("container");
console.log(containerDiv);

const lists = document.querySelectorAll("ul.list");

lists[0].children[1].textContent = "Richard";

lists[1].removeChild(lists[1].children[1]);

const myName = "Oumaima"; 
lists.forEach(ul => {
  ul.children[0].textContent = myName;
});

lists.forEach(ul => ul.classList.add("student_list"));

lists[0].classList.add("university", "attendance");

containerDiv.style.backgroundColor = "lightblue";
containerDiv.style.padding = "10px";

const secondUlLastLi = lists[1].children[lists[1].children.length - 1];
if (secondUlLastLi.textContent === "Dan") {
  secondUlLastLi.style.display = "none";
}

const richardLi = lists[0].children[1];
if (richardLi.textContent === "Richard") {
  richardLi.style.border = "2px solid black";
}

document.body.style.fontSize = "18px";

if (containerDiv.style.backgroundColor === "lightblue") {
  let users = [];
  lists.forEach(ul => {
    for (let li of ul.children) {
      if (li.style.display !== "none") {
        users.push(li.textContent);
      }
    }
  });
  alert(`Hello ${users.join(" and ")}`);
}
