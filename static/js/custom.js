$(document).ready(function () {
    // The first part of the code initializes the dropdown for books
    $(".nav-item.dropdown").hover(
      // When the mouse hovers over the .nav-item.dropdown element
      function () {
        // Slide down the dropdown menu inside of it
        $(this).find(".dropdown-menu").first().stop(true, true).slideDown();
      },
      // When the mouse leaves the .nav-item.dropdown element
      function () {
        // Slide up the dropdown menu inside of it
        $(this).find(".dropdown-menu").first().stop(true, true).slideUp();
      }
    );
  
    // The second part of the code initializes the dropdown for the user
    $(".dropdown-toggle").dropdown();
  
    // The third part of the code handles the user dropdown
    // When the .dropdown-toggle element is clicked
    $(".dropdown-toggle").on("click", function () {
      // Toggle the "show" class on the parent .dropdown element
      $(this).parent().toggleClass("show");
      // Toggle the "show" class on the sibling .dropdown-menu element
      $(this).siblings(".dropdown-menu").toggleClass("show");
    });
  
    // When a click event occurs anywhere on the document
    $(document).click(function (e) {
      // If the click did not occur inside of a .dropdown element
      if (!$(e.target).closest(".dropdown").length) {
        // Remove the "show" class from all .dropdown-menu elements
        $(".dropdown-menu").removeClass("show");
        // Remove the "show" class from all .dropdown elements
        $(".dropdown").removeClass("show");
      }
    });
  });
  