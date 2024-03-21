$(document).ready(function() {
    display_albums_list(results)

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



function display_albums_list(results) {
    let albumsList = $("#albums-list");
    albumsList.empty(); 

    let header = $("<div>").addClass("row results-header grey-text").text("Search Results for \"" + search_string + "\"");
    albumsList.append(header);

    if(results.length == 0){
        let row = $("<div>").addClass("row results light-grey-text bold-text").text("No results found.");
        albumsList.append(row);
        return
    } else if(results.length == 1) {
        let row = $("<div>").addClass("row results light-grey-text bold-text").text(results.length + " result found");
        albumsList.append(row);
    } else {
        let row = $("<div>").addClass("row results light-grey-text bold-text").text(results.length + " results found");
        albumsList.append(row);
    }

    for(let i = 0; i < results.length; i++) {
        let datum = results[i]
        var row = $("<div>").addClass("row no-gutters row-entry-spacing").attr("data-id", datum["id"]);
        let col1 = $("<div>").addClass("col-md-1");
        let col2 = $("<div>").addClass("col-md-11");
        let img = $("<img>").addClass("search-img img-fluid").attr("src", datum["cover_art"]).attr("alt", "Album cover art for " + datum["title"]);  

        var searchResult = datum["title"] + " (" + datum["release_year"] + ") - " + datum["artist"]


        let index = searchResult.toLowerCase().indexOf(search_string.toLowerCase());

        if (index !== -1) {
            let matchedSubstring = searchResult.substring(index, index + search_string.length);
            searchResult = searchResult.replace(matchedSubstring, "<span class='highlight'>" + matchedSubstring + "</span>");
        }

        let albumButton = $("<button>").addClass("album-btn").html(searchResult);

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