
function translate (text){
    if(text === '♔'){
        return 'K';
    }

    if(text === '♕'){
        return 'Q';
    }

    if(text === '♗'){
        return 'B';
    }

    if(text === '♘'){
        return 'N';
    }

    if(text === '♖'){
        return 'R';
    }

    if(text === '♙'){
        return 'P';
    }

    if(text === '♚'){
        return 'k';
    }

    if(text === '♛'){
        return 'q';
    }

    if(text === '♝'){
        return 'b';
    }

    if(text === '♞'){
        return 'n';
    }

    if(text === '♜'){
        return 'r';
    }

    if(text === '♟'){
        return 'p';
    }

    return text;
}

function set_position(position){
    $.each(position, function( index, value ) {
        $('#'+value[0]).html(value[1]);
    });
}

$(document).ready(function(){
    $('li').attr('draggable','true');
    $('.field').attr('draggable','true');

    $("li").on('click',function(){
        //alert("kli")
    });

    $('li').on('dragstart', function(e){
        event.dataTransfer.setData('text', e.target.id);
    })

    $('.field').on('dragstart', function(e){
        event.dataTransfer.setData('text', e.target.id);

    })


    $('.field').on('drop', function(e){
        e.preventDefault();
        // Get the data, which is the id of the drop target
        var data = e.originalEvent.dataTransfer.getData("text");

        $(this).text($('#'+data).text());
        if ($('#'+data).attr('class') === 'field'){
            $('#'+data).text('');
        }
    })

    $('.field').on('dragover', function(e){
        e.preventDefault();
    })

    $("#get-button").on('click',function(){
        var fields = [];
        var epd = "";
        var counter = 0;

        $('.field').each(function(){
            fields.push($(this).text())
        })

        for(i=0; i<fields.length; i++){
            if (fields[i] === ''){
                counter++;
            }   else {
                if (counter !== 0){
                    epd += counter + translate(fields[i]);
                }   else {
                    epd += translate(fields[i]);
                }
                counter=0;
            }

            if ( (i+1)%8 === 0 ){
                if (counter !== 0 ){
                    epd += counter +'/';
                }   else {
                    epd += '/';
                }
                counter = 0;
            }
        }
        $('input').val(epd);
    })

    $('#clear-button').on('click',function(){
        $('.field').each(function(){
            $(this).text('');
        })
    })

    $('#set-button').on('click',function(){
        $('.field').each(function(){
                $(this).text('  ');
        })

        $.post('',
        {
            epd: $('input').val(),
        },
        function(data){
            $('.field').each(function(){
                $(this).text(data[$(this).attr('id')]);
            })
        });
    })


})