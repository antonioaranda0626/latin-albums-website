$(document).ready(function(){
    var id = "";
    $('#add-album-form').submit(function(event){
        event.preventDefault();

        $('.error-message').remove();

        var durationPattern = /^\d{1,3}:\d{2}$/;
        var validInput = true;
        $('#add-album-form input, #add-album-form textarea').each(function() {
            if ($(this).val().trim() === '') {
                if(validInput){
                    $(this).focus();
                }
                validInput = false;
                $(this).addClass('error-field');
                $(this).after('<div class="error-message">Please fill out this field.</div>');
            }
            else if($(this).attr('id') === 'release_year' && isNaN($(this).val().trim())){
                $('.error-message').remove();
                if(validInput){
                    $(this).focus();
                }
                $(this).addClass('error-field');
                $(this).after('<div class="error-message">Please enter a valid year.</div>');
                validInput = false;
            }
            else if($(this).attr('id') === 'length' && !durationPattern.test($(this).val().trim())){
                if(validInput){
                    $(this).focus();
                }
                $(this).addClass('error-field');
                $(this).after('<div class="error-message">Please enter duration in MM:SS format.</div>');
                validInput = false;
            }
        });

        if (!validInput) {
            return;
        }

        var tracklist = $('#tracklist').val().split(',').map(function(item) { return item.trim(); });
        var featuredArtists = $('#featured_artists').val().split(',').map(function(item) { return item.trim(); });
        var genres = $('#genre').val().split(',').map(function(item) { return item.trim(); });

        var formData = {
            "title": $('#title').val().trim(),
            "artist": $('#artist').val().trim(),
            "release_year": $('#release_year').val(),
            "genre": genres,
            "tracklist": tracklist,
            "cover_art": $('#cover_art').val(),
            "featured_artists": featuredArtists,
            "label": $('#label').val(),
            "description": $('#description').val().trim(),
            "length": $('#length').val()
        };
        console.log(formData);

        $.ajax({
            type: 'POST',
            url: '/submit',
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(formData),
            success: function(response){
                $('#success-message').removeClass('d-none');
                $('#add-album-form')[0].reset();
                $('#title').focus();
                id = response.id;
            },
            error: function(xhr, status, error){
                alert('Error submitting data. Please try again.');
            }
        });
    });

    $('#view-item').click(function(){
        display_album_view(id)
    });

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
});

function display_album_view(id){
    $.ajax({
        type: "GET",
        url: '/view/' + encodeURIComponent(id),  
        contentType: "application/json; charset=utf-8",
        success: function(result){
            window.location.href = '/view/' + encodeURIComponent(id)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}