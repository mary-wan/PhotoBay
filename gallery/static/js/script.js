function copypath(id) {
    var path = document.getElementById(id);
    path.select();
    path.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(path.value);
    alert("Copied path: " + path.value);
  }
//   $(document).ready(function () {
//     $("imgdisplay").mouseover(function () {
//         $("#photoDesc").show();
//     });
//     $(".imgdisplay").mouseout(function () {
//         $("#photoDesc").hide();
//     });
//   });
