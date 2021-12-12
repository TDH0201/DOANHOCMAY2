const myParam = window.location.search.split('id=')[1];
console.log(myParam);
$( document ).ready(function() {
    console.log(myParam);
    $.ajax({

        type: 'GET',
        url: 'http://127.0.0.1:8000/api/book-detail/'+myParam+'/',
        success: function (data) {
            console.log(data.imgBookL);
            var figure =$('#figureBook');
            $(figure).empty();
            $(figure).append('<img src="'+data.imgBookM+'" alt="Girl in a jacket" class="img-bookM-detail" style="width: 100%; height: 100%;">')
                       
           var title = $('#bookdetail_title');
           $(title).empty();
           $(title).append(data.bookName);

           var author = $('#author_book');
           $(author).empty();
           $(author).append(data.Auth);

           var public = $('#year_public');
           $(public).empty();
           $(public).append(data.YearOfPublication);
        }
    });
});

