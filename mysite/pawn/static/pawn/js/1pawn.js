
var number = 1
$(document).ready(function(){
    $(".left").click(function(){
        if( number > 1 ){
            number -= 1;
        }
        $("#piece").attr("src",path+'piece'+number+'.jpg');
        $("#p"+number).css("display","block");
        $("#p"+(number+1)).css("display","none");
      });

    $(".right").click(function(){
        if( number < 6 ){
            number += 1;
        }
        $("#piece").attr("src",path+'piece'+number+'.jpg');

        $("#p"+number).css("display","block");
        $("#p"+(number-1)).css("display","none");
        //$("#msform").css("display","none");
      });
});