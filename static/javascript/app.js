const toggleButtons = document.querySelectorAll(".toggle-password");

toggleButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const input = button.parentElement.querySelector(".password-input");
    const icon = button.querySelector("i");

    if (input.type === "password") {
      input.type = "text";
      icon.classList.replace("fa-eye", "fa-eye-slash");
    } else {
      input.type = "password";
      icon.classList.replace("fa-eye-slash", "fa-eye");
    }
  });
});

const flashes = document.querySelectorAll(".flash-message");

flashes.forEach((flash) => {
  setTimeout(() => {
    flash.classList.add("hide");

    setTimeout(() => {
      flash.remove();
    }, 3000);
  }, 5000);
});

function toggleTheme() {
  const html = document.documentElement;

  html.classList.toggle("dark");

  if (html.classList.contains("dark")) {
    localStorage.setItem("theme", "dark");
  } else {
    localStorage.setItem("theme", "light");
  }
}

function toggleMenu() {
  const Menu = document.getElementById("mobile-menu");
  Menu.classList.toggle("hidden");
}

function copylink(id, button) {
  const link = document.getElementById(id);

  navigator.clipboard.writeText(link.href);

  const original = button.textContent;
  button.textContent = "Copied";

  setTimeout(() => {
    button.textContent = original;
  }, 2000);
}
