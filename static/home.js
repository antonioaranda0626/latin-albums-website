$(document).ready(function() {
    display_albums_list(data)

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

const favorites = ["2", "5", "8", "10"]

function display_albums_list(data) {
    let albumsList = $("#albums-list");
    albumsList.empty(); 


    for(let i = 0; i < favorites.length; i++) {
        let datum = data[favorites[i]]
        var row = $("<div>").addClass("row no-gutters row-entry-spacing").attr("data-id", datum["id"]);
        let col1 = $("<div>").addClass("col-md-1");
        let col2 = $("<div>").addClass("col-md-11");
        let img = $("<img>").addClass("search-img img-fluid").attr("src", datum["cover_art"]).attr("alt", "Album cover art for " + datum["title"]);  

        let albumButton = $("<button>").addClass("album-btn").text(datum["title"] + " (" + datum["release_year"] + ") - " + datum["artist"]);

        albumButton.click(function() {
            display_album_view(datum["id"]);
        })
        img.appendTo(col1);
        albumButton.appendTo(col2);

        col1.appendTo(row);
        col2.appendTo(row);

        albumsList.append(row);
    }
}

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