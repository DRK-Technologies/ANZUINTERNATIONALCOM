// === Slider ===
const slides = document.querySelectorAll(".slide");
const dots = document.querySelectorAll(".dot");
let index = 0;

function changeSlide() {
  if (index > slides.length - 1) index = 0;
  if (index < 0) index = slides.length - 1;

  for (let i = 0; i < slides.length; i++) {
	slides[i].style.display = "none";
	dots[i].classList.remove("active");
  }

  slides[index].style.display = "block";
  dots[index].classList.add("active");
}

function nextSlide(n) {
  index += n;
  changeSlide();
}

function prevSlide(n) {
  index += n;
  changeSlide();
}

function currentSlide(n) {
  index = n;
  changeSlide();
}

changeSlide();
setInterval(() => nextSlide(1), 4000);

// === Counter ===
document.addEventListener("DOMContentLoaded", () => {
    const counters = document.querySelectorAll('.counter');
  
    const formatNumber = (n) => {
      if (n >= 1000000000) return (n / 1000000000).toFixed(1) + 'B';
      if (n >= 1000000) return (n / 1000000).toFixed(1) + 'M';
      if (n >= 1000) return n.toLocaleString();
      return n;
    };
  
    const runCounter = (counter) => {
      const target = +counter.getAttribute('data-target');
      const step = +counter.getAttribute('data-step') || 1;
      const timeInterval = +counter.getAttribute('data-time-interval') || 100;
  
      const updateCount = () => {
        let current = +counter.innerText.replace(/[^0-9\.]/g, '');
        const increment = step;
  
        if (current < target) {
          counter.innerText = (current + increment).toFixed(
            counter.getAttribute('data-target') === '4.2' ? 1 : 0
          );
          setTimeout(updateCount, timeInterval);
        } else {
          counter.innerText = formatNumber(target);
        }
      };
  
      updateCount();
    };
  
    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          runCounter(entry.target);
          observer.unobserve(entry.target); // Run only once
        }
      });
    }, {
      threshold: 0.5 // Adjust if needed
    });
  
    counters.forEach(counter => {
      observer.observe(counter);
    });
  });
  
  