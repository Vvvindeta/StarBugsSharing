const accordionBtns = document.querySelectorAll('.accordion-btn')
accordionBtns.forEach(btn => {
    btn.addEventListener('click', function () {
        this.classList.toggle('active')
        const accordionDescription = this.nextElementSibling
        const plusIcon = this.querySelector('.plus-icon')
        const minusIcon = this.querySelector('.minus-icon')
        console.log(accordionDescription)
        if(accordionDescription.style.height) {
            accordionDescription.style.height = null
            plusIcon.style.display = 'block'
            minusIcon.style.display = 'none'
        } else {
            accordionDescription.style.height = accordionDescription.scrollHeight + 'px'
            plusIcon.style.display = 'none'
            minusIcon.style.display = 'block'
        }
    })
})

document.addEventListener('DOMContentLoaded', function() {
    var slogans = document.querySelectorAll('.hero-slogan h1');
    var link = document.querySelector('.hero-link');

    // Устанавливаем начальные стили для анимации
    slogans.forEach(function(slogan, index) {
        slogan.style.opacity = '0';
        slogan.style.animationDelay = index * 0.5 + 's'; // Задержка для каждого заголовка
        slogan.style.setProperty('--animate-duration', '5s');
    });

    // Запускаем анимацию заголовков
    slogans.forEach(function(slogan) {
        slogan.classList.add('animate__animated', 'animate__fadeIn');
    });
    link.style.setProperty('--animate-duration', '3s');
    // Запускаем анимацию для кнопки "Начать сейчас"
    setTimeout(function() {
        link.classList.add('animate__animated', 'animate__fadeIn');
        link.style.backgroundColor = 'black'
        link.style.fontWeight = 'bold'
        link.style.opacity = '1';
    }, slogans.length * 600); // Задержка для кнопки после всех заголовков
});
