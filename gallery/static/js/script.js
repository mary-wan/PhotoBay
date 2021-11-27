function copypath(id) {
    var path = document.getElementById(id);
    path.select();
    path.setSelectionRange(0, 99999); /* For mobile devices */
    navigator.clipboard.writeText(path.value);
    alert("Copied path: " + path.value);
  }
