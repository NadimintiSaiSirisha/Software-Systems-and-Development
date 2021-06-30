var myOptions = { };
var mySelect = $('#myDropdown');
$.each(myOptions, function(val, text) {
  mySelect.append(
      $('<option></option>').val(val).html(text)
  );
});


function dropFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}


$("#changeBG-btn").click(function(){
        $("body").css("background-image","url(https://cdn.glitch.com/529c37ea-ce17-4fa3-b654-74444a83d0d7%2FbackgroundSiri.png?v=1600772723076)"); 
      $("body").css("background-repeat", "no-repeat");
      $("body").css("background-size", "cover");
    });


    $("#threeAlert").keypress(function(e){
      if(e.which == 51 || e.which == 99){ //@ entered
        alert("Do not press 3 here!");
      }
    });

function blinkDeadline() {
    $('#blink').css("color", "red");
    $('#blink').fadeOut(200);
    $('#blink').fadeIn(200);
}
setInterval(blinkDeadline, 1000);


