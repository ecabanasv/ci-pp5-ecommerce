$(document).ready(function () {
  // Subcategory dropdown
  $("#subcategoryDropdown").on("change", function () {
    window.location.href = this.value;
  });
});
