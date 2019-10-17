
var number = 1
$(document).ready(function(){
    $(".left").click(function(){
        if( number > 2 ){
            number -= 1;
        }

        $("#piece").attr("src",path+'piece'+number+'.jpg');
      });

    $(".right").click(function(){
        if( number < 6 ){
            number += 1;
        }
        $("#piece").attr("src",path+'piece'+number+'.jpg');
      });
});