window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  var scrollButton = document.getElementById("scrollBtn");
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollButton.classList.remove("hidden"); // Удаляем класс "hidden", чтобы показать кнопку
    scrollButton.style.right = "20px"; // Устанавливаем отступ справа
  } else {
    scrollButton.classList.add("hidden"); // Добавляем класс "hidden", чтобы скрыть кнопку
  }
}

// Плавная прокрутка к верху страницы при нажатии на кнопку "Наверх"
function scrollToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
