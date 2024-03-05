// login.js
const passInput = document.getElementById("id_password");
const userNameInput = document.getElementById("id_username");

const inputs = [
    passInput,
    userNameInput,
];
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

const visibilityTrigger = document.querySelector(".visibilityTrigger");
var visible = false;
visibilityTrigger.addEventListener("click", () => {
  if (!visible) {
    passInput.type = "text";
    visibilityTrigger.innerHTML = "visibility_off";
    visible = true;
  } else {
    passInput.type = "password";
    visibilityTrigger.innerHTML;
    visible = false;
  }
});
