document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".home-action");
    const resultContainer = document.getElementById("result-container");
    const resultText = document.getElementById("result-text");
    const inputString = document.getElementById("inputString");

    buttons.forEach((button) => {
        button.addEventListener("click", async function () {
            // Replace the button text with the loading animation
            const originalText = button.textContent;
            button.innerHTML = `<div class="loading">Loading<span></span><span></span><span></span></div>`;
            button.disabled = true;

            const action = button.getAttribute("data-action");
            const input = inputString.value;

            if (!input.trim()) {
                alert("Please enter input before clicking a button.");
                button.innerHTML = originalText; // Reset button text
                button.disabled = false;
                return;
            }

            try {
                const response = await fetch('/aoc2015_solve', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        inputString: input,
                        action: action
                    })
                });

                if (!response.ok) throw new Error("Failed to fetch result from server.");

                const result = await response.text();

                // Display the result
                resultContainer.style.display = "block";
                resultText.innerHTML = result; // Use innerHTML to render newlines as <br>
            } catch (error) {
                console.error("An error occurred:", error);
                alert("An error occurred while processing your request.");
            } finally {
                // Reset button state
                button.innerHTML = originalText;
                button.disabled = false;
            }
        });
    });
});
