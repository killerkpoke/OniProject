// init
let slides = document.getElementsByClassName("mySlides");
// util func
function slideAnim(n, Xfrom, Xto, Ofrom, Oto) {
    anime({
        targets: slides[n],
        translateX: {
            value: [Xfrom, Xto],
            duration: 1500
        },
        opacity: {
            value: [Ofrom, Oto],
            duration: 1000
        },
        easing: 'easeInOutExpo',
        delay: 500,
    });
}

if (slides.length !== 0) {
    const delay = 4000
    let index = 0;
    slides[index].setAttribute('class', 'mySlides block');
    slideAnim(index, 100, 0, 0, 1);
    // loop
    const interval = setInterval(() => {
        index++
        if (slides.length > index) {
            slideAnim(index-1, 0, -100, 1, 0)
            setTimeout(() => {
                slides[index-1].setAttribute('class', 'mySlides hidden');
            }, 1500)
            setTimeout(() => {
                slides[index].setAttribute('class', 'mySlides block');
                slideAnim(index, 100, 0, 0, 1);
            }, 1500)
        }
        else {
            slideAnim(index-1, 0, -100, 1, 0)
            setTimeout(() => {
                slides[index-1].setAttribute('class', 'mySlides hidden');
                index = 0;
            }, 1500)
            setTimeout(() => {
                slides[index].setAttribute('class', 'mySlides block');
                slideAnim(index, 100, 0, 0, 1);
            }, 1500)
        }
    }, delay);
}
