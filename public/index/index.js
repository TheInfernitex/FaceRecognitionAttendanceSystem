const toggler = document.querySelector(".toggler");
const navMenu = document.querySelector("#navMenu");

toggler.addEventListener("click", function () {
  navMenu.classList.toggle("active");
});

const scroll = document.getElementById("scroll");

scroll.addEventListener("click", () => {
  document.querySelector(".get-started").scrollIntoView({ behavior: "smooth" });
});

document.addEventListener("DOMContentLoaded", () => {
  // Code inside this block will run after the HTML document has fully loaded
  document.getElementById("scanButton").addEventListener("click", () => {
    // Make a POST request to the server when the button is clicked
    fetch("/webcam_scan", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({}), // You can pass data if needed
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.message);
        // You can update the UI or display a message to the user as needed
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
});
