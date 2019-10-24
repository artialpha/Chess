var board = [];

for(i = 0; i < 8; i++){
    for(j = 0; j < 8; j++){
        var str = String.fromCharCode(65+i)+(j+1);
        board.push(str)
    }
}

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
    $('#'+move[0]).text('');
    $('#'+move[1]).text(pawn)
}




$(document).ready(function(){

    //$('#A5').html("&#9814;")

    set_position(final_position);

    $("#start").on("click", function(){
        clear_board(board);
        set_position(start_position);
        //alert("The paragraph was clicked.");
    });

    $(".move").on("click", function(){
        clear_board(board);
        set_position(start_position);
        var moves_elements = $(this).prevAll().addBack();
        var moves = [];
        $.each(moves_elements, function( index, value ) {
            var text = $(value).text();
            text = text.slice(3,text.length);
            alert(text);
            var first_field = text.slice(0,2).toUpperCase();
            var second_field = text.slice(2,4).toUpperCase();
            moves.push([first_field,second_field]);
        });

        $.each(moves,function(index, value){
            change_position(value);
        })
        //alert(moves[0])

    })




})