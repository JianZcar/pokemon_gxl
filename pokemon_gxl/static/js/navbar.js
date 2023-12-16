document.addEventListener('DOMContentLoaded', function() {
    var path = window.location.pathname;
    var page = path.split("/")[1];  // Get the second part of the URL path

    var navLinks = document.querySelectorAll('.navbar .btn');
    navLinks.forEach(function(link) {
        if (link.id === page) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');  // Remove the active class from other links
        }
    });
});

$(document).ready(function() {
    var url = window.location.pathname;
    $('.navbar a[href="' + url + '"]').addClass('active');
});