// carousel.js

const carousel = document.querySelector('.carousel');
const prevSlideButton = document.getElementById('prevSlide');
const nextSlideButton = document.getElementById('nextSlide');

let currentIndex = 0;
const slideWidth = carousel.querySelector('.carousel-slide').clientWidth;

function showSlide(index) {
    currentIndex = index;
    carousel.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
}

prevSlideButton.addEventListener('click', () => {
    if (currentIndex > 0) {
        showSlide(currentIndex - 1);
    }
});

nextSlideButton.addEventListener('click', () => {
    const numSlides = carousel.querySelectorAll('.carousel-slide').length;
    if (currentIndex < numSlides - 1) {
        showSlide(currentIndex + 1);
    }
});

// Inicializa o carrossel mostrando o primeiro slide
showSlide(0);
