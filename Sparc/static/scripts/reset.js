const emailInput = document.getElementById("id_email");

function checkEmptyInput(element) {
  const elementId = element.id;
  const elementLabel = document.querySelector(`label[for="${elementId}"]`); // Use backticks for string interpolation

  if (element.value.trim() !== "") {
    elementLabel.style.fontSize = ".75rem";
    elementLabel.style.top = "-10px";
  }
}
emailInput.addEventListener("blur", () => checkEmptyInput(emailInput));
