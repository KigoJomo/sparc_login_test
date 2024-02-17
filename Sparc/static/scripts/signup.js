// signup.js
const regInput = document.getElementById("id_reg_number");
const firstNameInput = document.getElementById("id_first_name");
const lastNameInput = document.getElementById("id_last_name");
const emailInput = document.getElementById("id_email");
const passInput1 = document.getElementById("id_password1");
const passInput2 = document.getElementById("id_password2");

const inputs = [
  regInput,
  firstNameInput,
  lastNameInput,
  emailInput,
  passInput1,
  passInput2,
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

// const visibilityTrigger = document.querySelectorAll(".visibilityTrigger");
// var visible = false;

// function makePasswordVisible(icon, password) {
//   password.type = visible ? "password" : "text";
//   visible = !visible;
//   icon.innerHtml

// }
// visibilityTrigger.forEach((trigger) => {
//   const passwordField = trigger.previousElementSibling.querySelector("input");
//   trigger.addEventListener("click", () => makePasswordVisible(trigger, passwordField));
// });
