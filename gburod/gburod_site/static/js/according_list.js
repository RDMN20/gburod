// var acc = document.getElementsByClassName("accordion");
// var i;
//
// for (i = 0; i < acc.length; i++) {
//   acc[i].addEventListener("click", function() {
//     this.classList.toggle("active");
//     var panel = this.nextElementSibling;
//     if (panel.style.maxHeight){
//       panel.style.maxHeight = null;
//     } else {
//       panel.style.maxHeight = panel.scrollHeight + "px";
//     }
//   });
// }

// function toggleDetails(detailsId) {
//     var details = document.getElementById(detailsId);
//     if (details.style.display === "none") {
//         details.style.display = "block";
//     } else {
//         details.style.display = "none";
//     }
// }

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