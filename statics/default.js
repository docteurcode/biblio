(function () {
    'use strict'
  
    document.querySelector('#navbarSideCollapse').addEventListener('click', function () {
      document.querySelector('.offcanvas-collapse').classList.toggle('open')
    })
  })()






  function filtreParClasse() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue, none;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    table = document.getElementById("container_elmnt");
    tr = table.getElementsByClassName("item");

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("em")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        // if (txtValue.toUpperCase().indexOf(filter)>-1) {
        //   tr[i].style.display = "";
        // } 
        if (txtValue.toUpperCase()==filter) {
          tr[i].style.display = "";
        } 
        
        else {
          tr[i].style.display = "none";
        }
      }
    }
  }

