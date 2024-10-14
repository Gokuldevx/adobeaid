/* Get the input field and suggestion box */
const inputField = document.querySelector("#search-input");
const suggestionsBox = document.querySelector(".suggestions");

/* list of Services */
const services = ["Carpentry", "Cleaning", "Electrician", "Gardening", "Home Nursing", "Home Renovation", "Home Salon", "Home Shifting", "Painting", "Pet Care", "Plumbing", "Repairing"];

/* Function to display suggestions */
function displaySuggestions() {
    const inputText = inputField.value.toLowerCase();
    const suggestions = services.filter(service => service.toLowerCase().startsWith(inputText));
    const html = suggestions.map(suggestion => `<li class="suggestion-item">${suggestion}</li>`).join(' ');
    suggestionsBox.innerHTML = html;
}

/* Event Listeners for input field */
inputField.addEventListener("input", () => {
    displaySuggestions();
    suggestionsBox.style.display = inputField.value? "block" : "none";
});

/* Event Listeners for suggestion item click */
suggestionsBox.addEventListener("click", (e) => {
    if (e.target.closest(".suggestion-item")) {
        inputField.value = e.target.innerText;
        suggestionsBox.style.display = "none";
    }
});

/* Close suggestions when clicking outside the search bar */
document.addEventListener("click",(e) => {
    if (!e.target.closest(".search-bar") && e.target!== suggestionsBox) {
        suggestionsBox.style.display = "none";
    }
});
