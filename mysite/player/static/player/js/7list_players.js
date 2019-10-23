


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
        //hej = parseInt($(this).parent().attr("id")); from clicked
        number_stars = parseInt($(this).parent().parent().prev().text().split(" ")[3]) // taken from paragraph from {{ user_rate|lookup:player.name }}
        if (number_stars >= 1 ){
            setStar(1, $(this).parent().children().eq(number_stars).get());
        }
    })


    $("ol.can-change li").click(function(){
        clickedIndex =  $(this).index() + 1;
        $(this).parent().attr("id",clickedIndex);
        setStar(1, this);
    })

    var element;
    $("ol.can-change li").click(function(){
        var rate = parseInt($(this).index());
        var name = $(this).parent().parent().parent().next().children().eq(1).text();
        name = name.trim().split(" ")[0];
        element = $(this);
        // $(this).parent().parent().parent().next().children().eq(1).text(); zwraca imie i nazwisko
        //$(this).parent().parent().parent().parent().children().get(); zwraca dwojke dzieci od TD
        $.post('/players',
        {
            name: name,
            rate:rate,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        function(data){
            var paragraph = element.closest('ol').prev(); // at first paragraph "your rate"
            var whole_text = paragraph.text();
            var text_changed = whole_text.slice(0,whole_text.length-1);
            text_changed += element.index();
            paragraph.text(text_changed);


            paragraph = paragraph.siblings('.average_rate'); // paragraph "averate rate"
            paragraph.text(data['average']);
            var star = paragraph.next();
            element = star.find('li').eq(Math.floor(data['average'])-1).get();
            //alert(star.find('li').eq(Math.floor(data['average'])).get());
            setStar(1,element );
            console.log(data);
        }
        );




    });






})