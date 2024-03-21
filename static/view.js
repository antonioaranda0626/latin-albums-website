$(document).ready(function() {
    $('form').submit(function(event) {
        event.preventDefault();
        let searchString = $(this).find('input[type="search"]').val().trim();
        if(searchString.length == 0){
            $(this).find('input[type="search"]').val("");
            $(this).find('input[type="search"]').focus();
        }
        else{
            $.ajax({
                type: "GET",
                url: '/search_results/' + encodeURIComponent(searchString),  
                contentType: "application/json; charset=utf-8",
                success: function(result){
                    window.location.href = '/search_results/' + encodeURIComponent(searchString)
                },
                error: function(request, status, error){
                    console.log("Error");
                    console.log(request)
                    console.log(status)
                    console.log(error)
                }
            });
        }
    });

    $('#edit-btn').click(function(){
        display_edit_view(result["id"])
    });

    $('.redirect-btn').click(function(){
        var searchString = $(this).text().trim();;
        $.ajax({
            type: "GET",
            url: '/search_results/' + encodeURIComponent(searchString),  
            contentType: "application/json; charset=utf-8",
            success: function(result){
                window.location.href = '/search_results/' + encodeURIComponent(searchString)
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    });
});

function display_edit_view(id){
    $.ajax({
        type: "GET",
        url: '/edit/' + encodeURIComponent(id),  
        contentType: "application/json; charset=utf-8",
        success: function(result){
            window.location.href = '/edit/' + encodeURIComponent(id)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}