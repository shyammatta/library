 

function validateLoginForm() {
    const password = document.getElementById('password').value;
    if (password.length < 4 || password.length > 8) {
        alert('Password must be between 4 and 8 characters.');
        return false;
    }
    return true;
}
document.addEventListener('DOMContentLoaded', function() {
    // Highlight selected checkboxes
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            if (checkbox.checked) {
                checkbox.parentElement.classList.add('selected'); // Add a 'selected' class to label
            } else {
                checkbox.parentElement.classList.remove('selected'); // Remove 'selected' class from label
            }
        });
    });

    // Form submission validation
    var form = document.getElementById('book-form');

    form.addEventListener('submit', function(event) {
        var checkedBoxes = form.querySelectorAll('input[type="checkbox"]:checked');

        if (checkedBoxes.length === 0) {
            alert('Please select at least one book category.');
            event.preventDefault(); // Prevent form submission if no checkbox is checked
        }
    });
});

//for selection of books
function disableSelectedBooks() {
    const selectedBooks = new Set();
    // Get the selected books from sessionStorage (if any)
    const storedBooks = JSON.parse(sessionStorage.getItem('selectedBooks')) || [];
    storedBooks.forEach(book => selectedBooks.add(book));
    
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        if (selectedBooks.has(checkbox.value)) {
            checkbox.disabled = true;
            checkbox.checked = true;
        }
        checkbox.addEventListener('change', function() {
            if (this.checked) {
                selectedBooks.add(this.value);
            } else {
                selectedBooks.delete(this.value);
            }
            // Store the selected books in sessionStorage
            sessionStorage.setItem('selectedBooks', JSON.stringify(Array.from(selectedBooks)));
        });
    });
}

window.onload = disableSelectedBooks;


// Function to calculate end date excluding weekends
function calculateEndDate(startDate, daysToAdd) {
    let endDate = new Date(startDate);
    
    for (let i = 0; i < daysToAdd; i++) {
        endDate.setDate(endDate.getDate() + 1); // Add one day
        
        // Skip weekends (Saturday and Sunday)
        if (endDate.getDay() === 0) { // Sunday
            endDate.setDate(endDate.getDate() + 1); // Skip to Monday
        } else if (endDate.getDay() === 6) { // Saturday
            endDate.setDate(endDate.getDate() + 2); // Skip to Monday
        }
    }
    
    return endDate;
}


// Function to update end date when start date is selected
function updateEndDate(input) {
    const row = input.closest('tr');
    const startDate = new Date(input.value);
    const endDate = calculateEndDate(startDate, 30);
    row.querySelector('input[name="end_date"]').value = endDate.toISOString().split('T')[0];
}

