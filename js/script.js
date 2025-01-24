let currentIndex = 0;

const items = document.querySelectorAll('.carousel-item');
const totalItems = items.length;
const carousel = document.getElementById('carousel');

// Función para mover al siguiente item del carrusel
function moveToNextItem() {
    currentIndex = (currentIndex + 1) % totalItems;
    carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
}

// Intervalo de tiempo para mover las imágenes automáticamente (5 segundos)
setInterval(moveToNextItem, 5000);
