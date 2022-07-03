$(document).ready(function(){
    


  $('.owl-carousel').owlCarousel({
   rtl:true,
   nav:true,
   dots:true,
   loop:true,
   margin:10,
   responsiveClass:true,
   responsive:{
       0:{
           items:1,
           nav:true
       },
       600:{
           items:2,
           nav:false
       },
       1000:{
           items:4,
           nav:true,
           loop:false
       }
   }
});


$('.tablinks').click(function(){
   $('.tablinks').removeClass('act');
   $(this).addClass('act');
});




});



function openTab(evt, Name) {
   // Declare all variables
   var i, tabcontent, tablinks;
 
   // Get all elements with class="tabcontent" and hide them
   tabcontent = document.getElementsByClassName("tabcontent");
   for (i = 0; i < tabcontent.length; i++) {
     tabcontent[i].style.display = "none";
   }
 
   // Get all elements with class="tablinks" and remove the class "active"
   tablinks = document.getElementsByClassName("tablinks");
   for (i = 0; i < tablinks.length; i++) {
     tablinks[i].className = tablinks[i].className.replace(" active", "");
   }
 
   // Show the current tab, and add an "active" class to the button that opened the tab
   document.getElementById(Name).style.display = "block";
   evt.currentTarget.className += " active";
 }


