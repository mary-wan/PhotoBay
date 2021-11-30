function copypath(id) {
    var path = document.getElementById(id);
    path.select();
    path.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(path.value);
    alert("Copied path: " + path.value);
  }

const navLinks = document.querySelectorAll('.nav-item')
const menuToggle = document.getElementById('navbarNavDropdown')
const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle:false})
navLinks.forEach((l) => {
      l.addEventListener('click', () => { bsCollapse.toggle() })
  })

function download(id) {
    var imagePath = document.getElementById(id);
    alert("yqq")
    let fileName = getFileName(imagePath);
    saveAs(imagePath, fileName);
  }

  // let btnDownload = document.getElementById('cl');
  // let img = document.getElementById('lol');


  // btnDownload.addEventListener('click', () => {
  //     let imagePath = img.getAttribute('src');
  //     let fileName = getFileName(imagePath);
  //     saveAs(imagePath, fileName);
  //     imagePath
  // });

  function getFileName(str) {
      return str.substring(str.lastIndexOf('/') + 1)
  }