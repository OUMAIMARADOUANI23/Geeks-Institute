const API_KEY = "cead0b9f79f628407c943f14";

const fromSelect = document.getElementById("from");
const toSelect = document.getElementById("to");
const amountInput = document.getElementById("amount");
const resultDiv = document.getElementById("result");
const convertBtn = document.getElementById("convert");
const switchBtn = document.getElementById("switch");

async function loadCurrencies() {
  const res = await fetch(`https://v6.exchangerate-api.com/v6/${API_KEY}/codes`);
  const data = await res.json();

  if (data.result === "success") {
    fromSelect.innerHTML = "";
    toSelect.innerHTML = "";

    data.supported_codes.forEach(([code, name]) => {
      const option1 = new Option(`${code} - ${name}`, code);
      const option2 = new Option(`${code} - ${name}`, code);
      fromSelect.add(option1);
      toSelect.add(option2);
    });

    fromSelect.value = "USD";
    toSelect.value = "MAD";
  } else {
    resultDiv.innerText = "Erreur lors du chargement des devises.";
  }
}

async function convert() {
  const from = fromSelect.value;
  const to = toSelect.value;
  const amount = amountInput.value;

  const res = await fetch(`https://v6.exchangerate-api.com/v6/${API_KEY}/pair/${from}/${to}/${amount}`);
  const data = await res.json();

  if (data.result === "success") {
    resultDiv.innerText = `${amount} ${from} = ${data.conversion_result.toFixed(2)} ${to}`;
  } else {
    resultDiv.innerText = "Conversion failed.";
  }
}

switchBtn.addEventListener("click", () => {
  const temp = fromSelect.value;
  fromSelect.value = toSelect.value;
  toSelect.value = temp;
  convert();
});

convertBtn.addEventListener("click", convert);
loadCurrencies();