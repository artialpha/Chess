


function setStar (number, element){
        $(element).prevAll().find(".star").attr("src",path+"star"+number+".png");
        $(element).find(".star").attr("src",path+"star"+number+".png");
        $(element).nextAll().find(".star").attr("src",path+"star0.png");
};

function classStar (text, element){
        $(element).prevAll().find(".star").attr("class",text);
        $(element).find(".star").attr("class",text);
};


$(document).ready(function(){
    var it;
    var clickedIndex=0;

    $(".hej").each(function(){
        it = Math.floor(parseFloat($(this).parent().children(':first-child').text()));
        setStar(1,$(this).siblings('ol').children(0)[it-1] );
    });


    $('ol.can-change li').hover(function(){
        setStar(1, this);
    },function(){
        setStar(0, this);
        hej = parseInt($(this).parent().attr("id"));
        if (hej >= 1 ){
            setStar(1, $(this).parent().children().eq(hej-1).get());
        }
    })


    $("ol.can-change li").click(function(){
        clickedIndex =  $(this).index() + 1;
        $(this).parent().attr("id",clickedIndex);
        setStar(1, this);
    })









})