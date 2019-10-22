


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

    // responsible for taking value from player.average_rating and putting value
    $(".hej").each(function(){
        it = Math.floor(parseFloat($(this).parent().children(':first-child').text()));
        setStar(1,$(this).siblings('ol').children(0)[it-1] );
    });

    $(".user").each(function(){
        number_stars = parseInt($(this).text().split(" ")[3]);
        li_element = $(this).next().children().children().eq(number_stars).get();
        setStar(1, li_element)
    })


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

    $("ol.can-change li").click(function(){
        var rate = parseInt($(this).index());
        var name = $(this).parent().parent().parent().next().children().eq(1).text();
        name = name.trim().split(" ")[0];
        // $(this).parent().parent().parent().next().children().eq(1).text(); zwraca imie i nazwisko
        //$(this).parent().parent().parent().parent().children().get(); zwraca dwojke dzieci od TD
        var thisUserAccount =
        $.post('/players',
        {
            name: name,
            rate:rate,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        }

        )

    });






})