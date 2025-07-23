const apiKey = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";
const form = document.getElementById("gifForm");
const input = document.getElementById("searchInput");
const gifContainer = document.getElementById("gifContainer");
const deleteAllBtn = document.getElementById("deleteAllBtn");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const query = input.value.trim();
  if (!query) return;

  try {
    const response = await fetch(`https://api.giphy.com/v1/gifs/random?tag=${query}&rating=g&api_key=${apiKey}`);
    if (!response.ok) throw new Error("Failed to fetch GIF");
    const data = await response.json();

    const gifUrl = data.data.images.fixed_height.url;

    const gifCard = document.createElement("div");
    gifCard.classList.add("gif-card");

    const img = document.createElement("img");
    img.src = gifUrl;
    img.alt = query;

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "DELETE";
    deleteBtn.addEventListener("click", () => gifCard.remove());

    gifCard.appendChild(img);
    gifCard.appendChild(deleteBtn);
    gifContainer.appendChild(gifCard);

    form.reset();
  } catch (error) {
    alert("Error fetching GIF: " + error.message);
    console.error(error);
  }
});

deleteAllBtn.addEventListener("click", () => {
  gifContainer.innerHTML = "";
});
