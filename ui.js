// Function to change text orientation
function changeTextOrientation(element, orientation) {
    document.querySelector(element).style.textOrientation = orientation;
}

// Example of adding styles dynamically
function applyStyles(element, styles) {
    Object.assign(document.querySelector(element).style, styles);
}

// Example of handling hover
document.querySelectorAll('.hover-effect').forEach(item => {
    item.addEventListener('mouseover', function() {
        this.style.opacity = 0.7;
    });
    item.addEventListener('mouseout', function() {
        this.style.opacity = 1;
    });
});

// Example of a slider
function slideElement(element, distance) {
    document.querySelector(element).style.transform = `translateX(${distance}px)`;
}

// Additional UI functions
function createProductCard(product) {
    return `
        <div class="product-card">
            <h3>${product.name}</h3>
            <p>${product.description}</p>
            <p>Price: $${product.price}</p>
        </div>
    `;
}

function createUserCard(user) {
    return `
        <div class="user-card">
            <h3>${user.name}</h3>
            <p>Email: ${user.email}</p>
        </div>
    `;
}
