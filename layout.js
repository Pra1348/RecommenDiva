// Flexbox layout functions
function applyFlexbox(element, direction = 'row', wrap = 'nowrap', justify = 'flex-start', align = 'stretch') {
    const el = document.querySelector(element);
    el.style.display = 'flex';
    el.style.flexDirection = direction;
    el.style.flexWrap = wrap;
    el.style.justifyContent = justify;
    el.style.alignItems = align;
}

// Applying max width and height
function setMaxSize(element, maxWidth, maxHeight) {
    const el = document.querySelector(element);
    el.style.maxWidth = maxWidth;
    el.style.maxHeight = maxHeight;
}

// Handling z-index
function setZIndex(element, zIndex) {
    document.querySelector(element).style.zIndex = zIndex;
}

// CSS Transform functions
function transformRotate(element, degrees) {
    document.querySelector(element).style.transform = `rotate(${degrees}deg)`;
}

function transformScale(element, scale) {
    document.querySelector(element).style.transform = `scale(${scale})`;
}

function transformSkew(element, degreesX, degreesY) {
    document.querySelector(element).style.transform = `skew(${degreesX}deg, ${degreesY}deg)`;
}

function transformTranslate(element, x, y) {
    document.querySelector(element).style.transform = `translate(${x}px, ${y}px)`;
}

// Additional layout functions
function createGrid(element, columns) {
    const el = document.querySelector(element);
    el.style.display = 'grid';
    el.style.gridTemplateColumns = `repeat(${columns}, 1fr)`;
}

function centerElement(element) {
    const el = document.querySelector(element);
    el.style.display = 'flex';
    el.style.justifyContent = 'center';
    el.style.alignItems = 'center';
}
