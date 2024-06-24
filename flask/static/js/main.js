document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("#recommendation-form");
  const input = document.querySelector("#username-input");
  const resultsTable = document.querySelector("#results-table");
  const errorText = document.querySelector("#error-text");
  const loadingIndicator = document.querySelector("#loading-indicator");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    // Clear previous results and error
    resultsTable.innerHTML = "";
    errorText.textContent = "";

    // Show loading indicator
    loadingIndicator.style.display = "block";

    // Fetch recommendations
    const username = input.value.trim();
    fetch(`/api/recommend?username=${username}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        // Hide loading indicator
        loadingIndicator.style.display = "none";

        if (data.error) {
          // Display specific error message returned from backend
          errorText.textContent = data.error;
        } else {
          // Display recommendations in a table
          const products = data.products;
          if (products.length > 0) {
            const tableRows = products
              .map((product) => `<tr><td>${product}</td></tr>`)
              .join("");
            resultsTable.innerHTML = `<table class="table"><tbody>${tableRows}</tbody></table>`;
          } else {
            resultsTable.innerHTML = "<p>No recommendations found.</p>";
          }
        }
      })
      .catch((error) => {
        // Hide loading indicator
        loadingIndicator.style.display = "none";

        // Display generic error message for unexpected errors
        errorText.textContent = `Error: ${error.message}`;
      });
  });
});
