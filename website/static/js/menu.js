const btn = document.getElementById('menuBtn');
const menu = document.getElementById("menuList");

btn.addEventListener("click", () => {
	menu.classList.toggle("hidden");
});