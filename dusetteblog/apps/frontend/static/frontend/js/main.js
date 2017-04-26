$( document ).ready(function() {
    function slides() {
        $(".slide-1 > .img-post-img").fadeIn().delay(5000).fadeOut();
        $(".slide-2 > .img-post-img").delay(5800).fadeIn().delay(5000).fadeOut();
        $(".slide-3 > .img-post-img").delay(12500).fadeIn().delay(5000).fadeOut(slides);
    }
    slides();
});