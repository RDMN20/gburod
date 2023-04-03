const stars = document.querySelectorAll('.rating .fa-star');
  const score = document.querySelector('#score');

  stars.forEach(star => {
    star.addEventListener('click', () => {
      const value = star.getAttribute('data-value');
      score.value = value;
      stars.forEach(star => star.classList.remove('checked'));
      for (let i = 0; i < value; i++) {
        stars[i].classList.add('checked');
      }
    });
  });
