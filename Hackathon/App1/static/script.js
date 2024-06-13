let currentSlide = 0;
const slides = document.querySelectorAll('.carousel img');
const indicators = document.querySelectorAll('.carousel-indicators button');
let slideInterval;

function showSlide(index) {
  slides[currentSlide].classList.remove('active');
  indicators[currentSlide].classList.remove('active');
  currentSlide = index;
  slides[currentSlide].classList.add('active');
  indicators[currentSlide].classList.add('active');
  resetSlideInterval();
}

function nextSlide() {
  let nextSlide = (currentSlide + 1) % slides.length;
  showSlide(nextSlide);
}

function prevSlide() {
  let prevSlide = (currentSlide - 1 + slides.length) % slides.length;
  showSlide(prevSlide);
}

function resetSlideInterval() {
  clearInterval(slideInterval);
  slideInterval = setInterval(nextSlide, 3000);
}

slideInterval = setInterval(nextSlide, 3000);
