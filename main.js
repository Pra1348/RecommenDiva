// Handling navigation and dynamic elements
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelectorAll('nav a').forEach(link => link.classList.remove('active'));
        this.classList.add('active');

        // Load the respective page content
        const page = this.getAttribute('href').substring(1);
        loadPageContent(page);
    });
});

// Load page content dynamically
function loadPageContent(page) {
    fetch(`/pages/${page}.html`)
        .then(response => response.text())
        .then(data => {
            document.querySelector('#content').innerHTML = data;
            // Initialize page-specific scripts if any
            if (page === 'products') {
                loadProducts();
            } else if (page === 'users') {
                loadUsers();
            }
        })
        .catch(error => console.error('Error loading page content:', error));
}

// Fetch products from the backend
function loadProducts() {
    fetch('/products')
        .then(response => response.json())
        .then(products => {
            const productContainer = document.querySelector('#product-container');
            productContainer.innerHTML = products.map(product => `
                <div class="product">
                    <h2>${product.name}</h2>
                    <p>${product.description}</p>
                    <p>Price: $${product.price}</p>
                </div>
            `).join('');
        })
        .catch(error => console.error('Error loading products:', error));
}

// Fetch users from the backend
function loadUsers() {
    fetch('/users')
        .then(response => response.json())
        .then(users => {
            const userContainer = document.querySelector('#user-container');
            userContainer.innerHTML = users.map(user => `
                <div class="user">
                    <h2>${user.name}</h2>
                    <p>Email: ${user.email}</p>
                </div>
            `).join('');
        })
        .catch(error => console.error('Error loading users:', error));
}

// Storage functions
function setItem(key, value) {
    localStorage.setItem(key, value);
}

function getItem(key) {
    return localStorage.getItem(key);
}

// Utility functions
function promptUser(message) {
    return prompt(message);
}

function showAlert(message) {
    alert(message);
}

// DRY Example
function logMessage(message) {
    console.log(message);
}

// Example usage
logMessage('Page Loaded');
