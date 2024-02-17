// reset_confirm.js
const newPassInput = document.getElementById("id_new_password1");
const newPassInput2 = document.getElementById("id_new_password2");

const inputs = [newPassInput, newPassInput2];
function checkEmptyInput(element) {
  const elementId = element.id;
  const elementLabel = document.querySelector(`label[for="${elementId}"]`); // Use backticks for string interpolation

  if (element.value.trim() !== "") {
    elementLabel.style.fontSize = ".75rem";
    elementLabel.style.top = "-10px";
  }
}

//Add blur event listener to all inputs at once
inputs.forEach((input) => {
  input.addEventListener("blur", () => checkEmptyInput(input));
  console.log("blurred");
});
