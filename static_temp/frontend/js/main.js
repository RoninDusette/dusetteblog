$(document).ready(function () {
    $('a.slide-1').fadeIn(5000).removeClass('hidden', function () {
            $('a.slide-1').fadeOut(1000).addClass('hidden');
    });
});