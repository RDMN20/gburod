$(document).ready(function() {
  if (window.innerWidth < 768) {
    $(".preview-link").each(function() {
      var href = $(this).attr("href");
      $(this).removeAttr("data-toggle");
      $(this).removeAttr("data-target");
      $(this).click(function(e) {
        e.preventDefault();
        window.open(href, "_blank");
      });
    });
  }
});
