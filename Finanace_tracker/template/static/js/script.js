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
