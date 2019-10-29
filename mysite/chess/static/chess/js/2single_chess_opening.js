var board = [];

for(i = 0; i < 8; i++){
    for(j = 0; j < 8; j++){
        var str = String.fromCharCode(65+i)+(j+1);
        board.push(str)
    }
}

//
function set_position(position){
    $.each(position, function( index, value ) {
        $('#'+value[0]).html(value[1]);
    });
}

function clear_board(position){
    $.each(position, function( index, value ) {
        $('#'+value).html('');
    });
}

function change_position(move){
    var pawn = $('#'+move[0]).text();
    //castlings
    if ( move[0] == 'E1' && move[1] == 'G1'){
        $('#H1').text('');
        $('#F1').text('♖')
    }

    if ( move[0] == 'E1' && move[1] == 'C1'){
        $('#A1').text('');
        $('#D1').text('♖')
    }

    if ( move[0] == 'E8' && move[1] == 'G8'){
        $('#H8').text('');
        $('#F8').text('♖')
    }

    if ( move[0] == 'E8' && move[1] == 'C8'){
        $('#A8').text('');
        $('#D8').text('♖')
    }
    $('#'+move[0]).text('');
    $('#'+move[1]).text(pawn)
}

function get_fields(text){
    var fields = []
    text = text.slice(3,text.length);
    fields[0] = text.slice(text.length-4,text.length-2).toUpperCase();
    fields[1] = text.slice(text.length-2,text.length).toUpperCase();
    return fields;
}

function change_color(element, color){
    var elements = $(element).parent().siblings();
    //alert(elements.get());

    $.each(elements, function(){
        $(this).children().css('color','');
        //alert($(this).children().text())
    })


    $(element).css("color",color);
}

function calculate_position(element){
        clear_board(board);
        set_position(start_position);

        var moves_elements = $(element).parent().prevAll().addBack();
        var moves = [];
        $.each(moves_elements, function( index, value ) {
            //alert($(value).children().text())
            var text = $(value).children().text();
            var fields = get_fields(text)
            moves.push(fields);
        });
        moves.shift() // to get rid of start row
        $.each(moves,function(index, value){
            change_position(value);
        })
        change_color(element,"blue");
}

function calculate_start(element){
    clear_board(board);
    set_position(start_position);
    $(element).css("color","blue");
    $(".move").css("color","");
}


$(document).ready(function(){

    //$('#A5').html("&#9814;")
    $(".move").last().  css("color","blue"); // next because i don't know why but it couldn't get "the last"
    set_position(final_position);

    $("#start").on("click", function(){
        calculate_start(this)
    });

    $(".move").on("click", function(){
        calculate_position(this)
    })


    $(".left").on('click', function(){
        var element = $('.move').filter(function() {
            //alert($(this).css('color'))
            return $(this).css('color') == 'rgb(0, 0, 255)';
        });
        element = element.parent().prev().children();
        calculate_position(element);
    })

    $(".right").on('click', function(){
        var element = $('.move').filter(function() {
            //alert($(this).css('color'))
            return $(this).css('color') == 'rgb(0, 0, 255)';
        });

        if (element.parent().index() !== ($('.move').length-1)){
            element = element.parent().next().children();
            calculate_position(element);
        }


    })





})