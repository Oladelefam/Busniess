// select input and list items
const searchInput = document.getElementById("searchInput");
const items = document.querySelectorAll("#itemList li");

// filter items as user types
searchInput.addEventListener("keyup", function() {
  const searchValue = searchInput.value.toLowerCase();

  items.forEach(function(item) {
    const text = item.textContent.toLowerCase();
    item.style.display = text.includes(searchValue) ? "" : "none";
  });
});

document.addEventListener("DOMContentLoaded", function () {

     // active nav link

    const navLinks = document.querySelectorAll(".nav-link");
    const currentPage = window.location.pathname;

    navLinks.forEach(link => {
        if (currentPage.includes(link.getAttribute("href"))) {
            link.classList.add("active-nav");
        }
    });

    //dashboard colour balance

    const balanceElement = document.querySelector(".amount");

    if (balanceElement) {
        const value = parseFloat(balanceElement.textContent.replace("$", ""));

        if (!isNaN(value)) {
            balanceElement.style.color =
                value < 0 ? "#e53935" : "#2EC4B6";
        }
    }

  

    // pade fade in

    document.body.classList.add("loaded");

     // dark mode 

    const toggle = document.getElementById("darkToggle");

    if (toggle) {
        toggle.addEventListener("click", function () {
            document.body.classList.toggle("dark-mode");

            localStorage.setItem(
                "darkMode",
                document.body.classList.contains("dark-mode")
            );
        });

        if (localStorage.getItem("darkMode") === "true") {
            document.body.classList.add("dark-mode");
        }
    }

});
