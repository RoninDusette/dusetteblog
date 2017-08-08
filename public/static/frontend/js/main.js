$(document).ready(function(){
  $('.bxslider').bxSlider({
      auto: true,
      mode: 'fade',
      speed: 900
  });
});

$(document).ready(function () {
   $(".home-title").slideDown("600").fadeIn("slow", function () {
       $(".home-subtitle").slideUp("slow").fadeIn("slow");
   });
});