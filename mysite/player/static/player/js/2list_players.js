


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


    // responsible for user's rate
    $(".user").each(function(){
        number_stars = parseInt($(this).text().split(" ")[3]);
        li_element = $(this).next().find('li').eq(number_stars-1).get();
        setStar(1, li_element)
    })


    $('ol.can-change li').hover(function(){
        setStar(1, this);
    },function(){
        setStar(0, this);
        //hej = parseInt($(this).parent().attr("id")); from clicked
        number_stars = parseInt($(this).parents('ol').prev().text().split(" ")[3]) // taken from paragraph from {{ user_rate|lookup:player.name }}

        if (number_stars >= 1 ){
            setStar(1, $(this).parent().children().eq(number_stars-1).get());
        }
    })




    var element;
    $("ol.can-change li").click(function(){
        var rate = parseInt($(this).index())+1;
        var name = $(this).parents('ol').prev().text(); // get text from paragraph < name >
        //alert($(this).parents('ol').prev().text())
        name = name.trim().split(" ")[2]; // get name
        element = $(this);

        $.post('/players',
        {
            name: name,
            rate:rate,
        },
        function(data){

            var paragraph = element.closest('ol').prev(); // at first paragraph "your rate"
            var whole_text = paragraph.text();
            var text_changed = whole_text.slice(0,whole_text.length-1);
            var value = element.index()+1
            text_changed += value;
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