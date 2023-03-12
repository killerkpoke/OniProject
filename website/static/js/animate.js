const main_title = document.getElementById("main-title");
const second_title = document.getElementById("second-title");
const main_desc = document.getElementById("main-desc");
const elements = document.getElementsByClassName("anime-text");
const cards = document.getElementsByClassName("anime-card");
const about_texts = document.getElementsByClassName("about-text");

// Home page main title
anime({
  targets: main_title,
  scale: [0, 0.8],
  duration: 1500,
  delay: 250,
  easing: 'easeInOutExpo'
});
// Second Title and Main Desc. on home page
let home_anim = (w, from, to) => anime({
  targets: w,
    translateX: {
        value: [from, to],
        duration: 2000,
        delay: 1500
    },
  scale: {
        value: [0, 1],
        duration: 1500,
        easing: 'easeInOutQuart'
    },
    delay: 1000,
});
home_anim(second_title, 600, 0);
home_anim(main_desc, -600, 0);

// Title of the subpages
anime({
  targets: elements,
  scale: [0, 0.8],
  duration: 3000,
  delay: 500,
});
// Card elements in the subpages based on how many elements we have
let anim = (w, d) => anime({
    targets: w,
    translateY: {
        value: [200, 0],
        duration: 1500
    },
    scale: {
        value: [0, 1],
        duration: 2000,
        easing: 'easeInOutExpo'
    },
    delay: d,
})
if (cards.length == 1) anim(cards, 250);
else anim(cards, anime.stagger(250, {easing: 'easeOutQuad'}));

// About page
home_anim(about_texts, 0, 0);

