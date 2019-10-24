

$(document).ready(function(){
    $(".button_active").click(function(){
        var open_name = $(".text").val();
        //alert($(".text").val());

        $.post('',
        {
            'open_name': open_name,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        function(data){
            //alert(data['open_id'])
            var path = window.location.pathname+data['open_id']
            //alert(window.location.pathname)
            window.open(data['open_id'])
        })
    })

    //Amar Gambit

})