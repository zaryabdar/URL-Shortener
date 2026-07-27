    const flashes = document.querySelectorAll(".flash-message");

    flashes.forEach((flash)=>{
        setTimeout(()=>{
            flash.classList.add("hide");

            setTimeout(()=>{
                flash.remove();
            },3000)
        },5000);
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

function toggleMenu(){
    const Menu = document.getElementById('mobile-menu')
    Menu.classList.toggle("hidden")
}

if (localStorage.getItem("theme") === "dark") {
    document.documentElement.classList.add("dark");
} else {
    document.documentElement.classList.remove("dark");
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