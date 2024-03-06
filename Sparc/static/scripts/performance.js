const scrollLeftButton = document.getElementById("scrollLeft");
const scrollRightButton = document.getElementById("scrollRight");
const scrollContainer = document.getElementById("details");

scrollLeftButton.addEventListener("click", () => {
  scrollContainer.scrollLeft -= scrollContainer.offsetWidth;
});
scrollRightButton.addEventListener("click", () => {
  scrollContainer.scrollLeft += scrollContainer.offsetWidth;
});

function getGrade(parameter) {
  let gradeToReturn;

  if (70 <= parameter && parameter <= 100) {
    gradeToReturn = "A";
  } else if (60 <= parameter && parameter <= 69) {
    gradeToReturn = "B";
  } else if (50 <= parameter && parameter <= 59) {
    gradeToReturn = "C";
  } else if (40 <= parameter && parameter <= 49) {
    gradeToReturn = "D";
  } else if (0 <= parameter && parameter <= 39) {
    gradeToReturn = "E";
  }

  return gradeToReturn;
}


const lists = document.querySelectorAll(".list");
lists.forEach((list) => {
  let total = 0
  let counter = 0

  const scores = list.querySelectorAll(".record .score")
  scores.forEach((score) => {
    let score_to_add = parseInt(score.innerHTML);
    total = total + score_to_add
    counter ++
  })
  const avg = list.querySelector(".record .avg")
  const grd = list.querySelector(".record .grd")
  console.log(`${total} : ${counter}`)
  let average_dec = total / counter;
  let average = average_dec.toFixed(1)
  let grade = getGrade(average);
  avg.innerHTML = average;
  grd.innerHTML = grade;
})
