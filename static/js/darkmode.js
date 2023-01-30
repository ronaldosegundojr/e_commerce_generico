let darkMode = false;

function switchMode() {
    const body = document.querySelector("body");
    const darkModeSwitch = document.querySelector("#dark-mode-switch");

    if (darkMode) {
        body.classList.remove("dark");
        darkModeSwitch.innerText = "Dark Mode";
        darkMode = false;
    } else {
        body.classList.add("dark");
        darkModeSwitch.innerText = "Light Mode";
        darkMode = true;
    }
}