function toggleDetails(sectionId) {
    var details = document.getElementById(sectionId);
    var accordions = document.getElementsByClassName('accordion');
    for (var i = 0; i < accordions.length; i++) {
        var currentDetails = accordions[i].nextElementSibling;
        if (currentDetails.id !== sectionId) {
            currentDetails.style.display = 'none';
            accordions[i].classList.remove('active');
        }
    }
    details.style.display = details.style.display === "block" ? "none" : "block";
    document.querySelector('[onclick="toggleDetails(\'' + sectionId + '\')"]').classList.toggle("active");
}

function toggleSubmenu(event, submenuId) {
    var submenu = document.getElementById(submenuId);
    if (submenu.style.display === '' || submenu.style.display === 'none') {
      submenu.style.display = 'block';
    } else {
      submenu.style.display = 'none';
    }
  }