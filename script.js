document.addEventListener('DOMContentLoaded', function() {
    const gameItems = document.querySelectorAll('.game-item');
    const message = document.querySelector('.message');
    const congratsMessage = document.querySelector('.congrats-message');
    let foundItems = 0;

    gameItems.forEach(item => {
        item.addEventListener('click', function() {
            if (!item.classList.contains('found')) {
                item.classList.add('found');
                message.style.display = 'block';
                setTimeout(() => {
                    message.style.display = 'none';
                }, 2000);

                foundItems++;
                if (foundItems === gameItems.length) {
                    setTimeout(() => {
                        congratsMessage.style.display = 'block';
                    }, 2000);
                }
            }
        });
    });
});
