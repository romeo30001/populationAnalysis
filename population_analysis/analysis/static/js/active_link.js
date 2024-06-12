document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            // Remove 'active' class from all nav-links
            navLinks.forEach(navLink => navLink.classList.remove('active'));
            // Add 'active' class to the clicked nav-link
            this.classList.add('active');
            // Save href of the active link in localStorage
            localStorage.setItem('activeLink', this.getAttribute('href'));
        });
    });

    // Check which link was active previously
    const activeLinkHref = localStorage.getItem('activeLink');
    if (activeLinkHref) {
        navLinks.forEach(link => {
            if (link.getAttribute('href') === activeLinkHref) {
                link.classList.add('active');
            }
        });
    }
});