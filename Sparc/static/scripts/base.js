document.addEventListener("DOMContentLoaded", function () {
  var currentUrl = window.location.pathname;
  var navLinks = document.querySelectorAll("nav > .menu-item");

  navLinks.forEach((link) => {
    var linkUrl = link.getAttribute("href");

    if (currentUrl === linkUrl) {
      navLinks.forEach((otherLink) => {
        otherLink.classList.remove("active");
      });
      link.classList.add("active");
    }
  });
});
const tint = document.querySelector(".tint");
const profileButton = document.querySelector(".profile-button");
const profileOverlay = document.querySelector(".profile_overlay");
const closeOverlay = document.querySelector(".close");
profileButton.addEventListener("click", () => {
  tint.style.display = "block";
  profileOverlay.style.display = "flex";
});
tint.addEventListener("click", () => {
  tint.style.display = "none";
  profileOverlay.style.display = "none";
});
closeOverlay.addEventListener("click", () => {
  tint.style.display = "none";
  profileOverlay.style.display = "none";
});
