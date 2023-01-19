// Get the navbar element
var navbar = document.querySelector('.navbar');

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function showHideNavBar() {
  if (window.pageYOffset > sticky) {
    navbar.classList.add("visible");
  } else {
    if (location.pathname == "/") {
      navbar.classList.remove("visible");
    }
  }
}

// When the user scrolls the page, execute showHideNavBar
window.onscroll = function() {showHideNavBar()};
