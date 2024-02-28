const dateElement = document.getElementById("dateElement");
const timeElement = document.getElementById("timeElement");

// Function to format the current date as "Day, Date, Month"
function getCurrentDate() {
  const daysOfWeek = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];
  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  const currentDate = new Date();
  const dayOfWeek = daysOfWeek[currentDate.getDay()];
  const dayOfMonth = currentDate.getDate();
  const month = months[currentDate.getMonth()];

  const formattedDate = `${dayOfWeek}, ${dayOfMonth}, ${month}`;
  return formattedDate;
}

// Function to get the current time in 12-hour format
function getCurrentTime12Hour() {
  const currentTime = new Date();
  let hours = currentTime.getHours();
  const minutes = currentTime.getMinutes();
  const ampm = hours >= 12 ? "PM" : "AM";

  // Convert hours to 12-hour format
  hours = hours % 12 || 12;

  const formattedTime = `${hours}:${minutes < 10 ? "0" : ""}${minutes} ${ampm}`;
  return formattedTime;
}
function updateTime() {
  const timeElement = document.getElementById("timeElement");
  timeElement.innerText = getCurrentTime12Hour();
}

updateTime();
setInterval(updateTime, 60000);
dateElement.innerHTML = getCurrentDate();


//to display the CALENDAR
document.addEventListener("DOMContentLoaded", function () {
  const currentMonthElement = document.getElementById("currentMonth");
  const prevMonthButton = document.getElementById("prevMonth");
  const nextMonthButton = document.getElementById("nextMonth");
  const daysContainer = document.querySelector(".dates");

  let currentDate = new Date();

  function renderCalendar() {
    const currentMonth = currentDate.toLocaleString("default", {
      month: "long",
    });
    currentMonthElement.textContent = currentMonth;

    const daysInMonth = new Date(
      currentDate.getFullYear(),
      currentDate.getMonth() + 1,
      0
    ).getDate();
    const firstDayOfMonth = new Date(
      currentDate.getFullYear(),
      currentDate.getMonth(),
      1
    ).getDay();

    daysContainer.innerHTML = "";

    for (let i = 0; i < firstDayOfMonth; i++) {
      const emptyDay = document.createElement("div");
      emptyDay.classList.add("day");
      daysContainer.appendChild(emptyDay);
    }

    for (let i = 1; i <= daysInMonth; i++) {
      const dayElement = document.createElement("div");
      dayElement.classList.add("day");
      dayElement.textContent = i;

      if (
        i === new Date().getDate() &&
        currentDate.getMonth() === new Date().getMonth()
      ) {
        dayElement.classList.add("today");
      }

      daysContainer.appendChild(dayElement);
    }
  }

  renderCalendar();

  prevMonthButton.addEventListener("click", function () {
    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar();
  });

  nextMonthButton.addEventListener("click", function () {
    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar();
  });
});

