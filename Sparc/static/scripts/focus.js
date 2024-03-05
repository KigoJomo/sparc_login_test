const setTimerParagraph = document.querySelector(".set_timer");
const timerParagraph = document.querySelector(".timer");
const startTimerButton = document.getElementById("start_session");
const pauseTimerButton = document.getElementById("pauseTimer");
const continueTimerButton = document.getElementById("continueTimer");
const terminateTimerButton = document.getElementById("terminateTimer");
const durationPargraph = document.getElementById("duration_paragraph");
const progressIndicator = document.getElementById("progressIndicator");
const timerCompleteSound = document.getElementById("timerCompleteSound");
const SessionDurationInput = document.getElementById("SessionDurationInput");
const breaks_info = document.getElementById("breaks_info");
function updateBreaksInfo() {
  let desiredSession = parseInt(SessionDurationInput.value);
  let idealSession =
    parseInt(document.getElementById("id_focus_period").value) +
    parseInt(document.getElementById("id_break_duration").value);
  let breaks = desiredSession / idealSession;
  if (breaks === 1) {
    breaks_info.innerHTML = "You'll have one break";
  } else {
    breaks_info.innerHTML = `You'll have ${breaks} breaks`;
  }
}
updateBreaksInfo();
const incrementButton = document.getElementById("increment");
const decrementButton = document.getElementById("decrement");
incrementButton.addEventListener("click", () => {
  SessionDurationInput.stepUp();
  updateBreaksInfo();
});
decrementButton.addEventListener("click", () => {
  SessionDurationInput.stepDown();
  updateBreaksInfo();
});
//hidden input for  form submission
const id_session_duration_mins = document.getElementById(
  "id_session_duration_mins"
);
const id_session_duration_sec = document.getElementById(
  "id_session_duration_sec"
);

let daily_goal = parseInt(document.getElementById("id_daily_goal").value);
let mins, sec;
let timerInterval;
// Variable to store the remaining time
let remainingTime;
let startTime; // Variable to store the start time of the session
let endTime;
let isTimerPaused = false;

function startTimer() {
  isTimerPaused = false;
  setTimerParagraph.style.display = "none";
  timerParagraph.style.display = "flex";
  let focus_period = parseInt(document.getElementById("id_focus_period").value);
  let break_period = parseInt(
    document.getElementById("id_break_duration").value
  );
  let desiredSession = parseInt(SessionDurationInput.value);
  let idealSession = focus_period + break_period;
  let numberOfBreaks = desiredSession / idealSession;
  let numberOfPeriods = numberOfBreaks - 1;

  // If there is remaining time, use it; otherwise, initialize minutes and seconds
  if (remainingTime) {
    [mins, sec] = remainingTime;
  } else {
    mins = focus_period - 1;
    sec = 59;
  }

  // Store the start time when starting the timer
  startTime = new Date();

  // Set up an interval that runs every second
  timerInterval = setInterval(function () {
    // Format minutes and seconds with leading zeros if needed
    let formattedMinutes = mins < 10 ? `0${mins}` : mins;
    let formattedSeconds = sec < 10 ? `0${sec}` : sec;

    // Update the UI with the current time
    durationPargraph.innerText = formattedMinutes + ":" + formattedSeconds;
    progressIndicator.style.height = `${
      100 - ((mins * 60 + sec) / (focus_period * 60)) * 100
    }%`;

    // Check if the timer has reached 00:00
    if (mins === 0 && sec === 0) {
      timerCompleteSound.play();

      // Toggle between focus period and break
      if (numberOfBreaks === numberOfPeriods && numberOfPeriods > 0) {
        // If there are remaining breaks, reset the countdown for the break
        mins = focus_period;
        sec = 0;
        numberOfPeriods--; // Decrease the number of remaining breaks
      } else if (numberOfBreaks > numberOfPeriods && numberOfBreaks > 0) {
        mins = break_period;
        sec = 0;
        numberOfBreaks--;
      } else if (numberOfBreaks === 0 && numberOfPeriods === 0) {
        // If not, stop the timer
        clearInterval(timerInterval);
        endTime = new Date();
        pauseTimerButton.style.display = "none";
        isTimerPaused = true;
      }
    }

    // Update minutes and seconds based on the countdown logic
    if (sec === 0) {
      mins--;
      sec = 59;
    } else {
      sec--;
    }

    // Store the remaining time when pausing
    remainingTime = [mins, sec];
  }, 1000); // The interval runs every 1000 milliseconds (1 second)
}

function pauseTimer() {
  continueTimerButton.style.display = "flex";
  pauseTimerButton.style.display = "none";
  isTimerPaused = true;
  clearInterval(timerInterval);
}

function continueTimer() {
  continueTimerButton.style.display = "none";
  pauseTimerButton.style.display = "flex";
  isTimerPaused = false;
  startTimer();
}

function terminateTimer() {
  clearInterval(timerInterval);
  isTimerPaused = true;

  // Calculate session duration
  if (typeof endTime === "undefined") {
    endTime = new Date();
  }
  const sessionDuration = Math.floor((endTime - startTime) / 1000); // in seconds

  // Convert seconds to minutes and update the hidden_session_duration element
  const minutes = Math.floor(sessionDuration / 60);
  const seconds = sessionDuration % 60;
  id_session_duration_mins.value = `${minutes}`;
  console.log(id_session_duration_mins.value);
  id_session_duration_sec.value = `${seconds}`;
  console.log(id_session_duration_sec.value);

  setTimerParagraph.style.display = "flex";
  timerParagraph.style.display = "none";
  // Reset remaining time when terminating
  remainingTime = undefined;
}

startTimerButton.addEventListener("click", startTimer);
pauseTimerButton.addEventListener("click", pauseTimer);
continueTimerButton.addEventListener("click", continueTimer);
terminateTimerButton.addEventListener("click", terminateTimer);
document.addEventListener("keydown", function (event) {
  if (event.key === " ") {
    if (timerParagraph.style.display === "flex") {
      if (
        pauseTimerButton.style.display === "flex" ||
        continueTimerButton.style.display === "flex"
      ) {
        if (isTimerPaused) {
          continueTimer();
        } else {
          pauseTimer();
        }
      }
    }
  }
});
