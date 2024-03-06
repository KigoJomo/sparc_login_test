document.addEventListener("DOMContentLoaded", function () {
  const addTaskButton = document.getElementById("add_task_button");
  const tint = document.getElementById("tint");
  const taskCreationForm = document.getElementById("task_creation_form");
  const taskAdded = document.getElementById("task_added");

  function closeForm() {
    tint.style.display = "none";
    taskCreationForm.style.display = "none";
    taskCreationForm.style.right = "-50%";
  }

  function validateForm() {
    const titleInput = document.getElementById("id_title");
    const descriptionInput = document.getElementById("id_description");
    const unitInput = document.getElementById("id_unit");
    const dateInput = document.getElementById("id_due_date");

    const inputsEmpty =
      titleInput.value.trim() === "" ||
      descriptionInput.value.trim() === "" ||
      unitInput.value.trim() === "" ||
      dateInput.value.trim() === "";

    return !inputsEmpty;
  }

  function closeMenuOrNot(event) {
    if (!validateForm()) {
      event.preventDefault();
      window.alert(
        "Oops!! Looks like we missed something. Let's try that again"
      );
    } else {
      closeForm();
      window.alert("Your  Task has been added successfully!");
    }
  }

  addTaskButton.addEventListener("click", () => {
    tint.style.display = "block";
    taskCreationForm.style.display = "flex";
    taskCreationForm.style.right = "0";
  });

  tint.addEventListener("click", closeForm);
  taskAdded.addEventListener("click", closeMenuOrNot);
});


