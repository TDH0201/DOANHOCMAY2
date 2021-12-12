$( document ).ready(function() {
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/api/Book/',
        success: function (data) {
            var editchoice =$('#edit-choice');
            $(editchoice).empty();
            for (i=10; i<16 ;i++){
                $(editchoice).append(' <div class="col-md-2">' + 
                '<div class="card " style="width: 172px ; height: 294px; border: none;">'+
                '  <img onclick="Bookdetail('+data[i].id+')" id="book-detailss"  src=" '+ data[i].imgBookM + ' " class="card-img-top card-img-book" alt="the boss">'+
                ' <div class="card-body " >'+
                ' <p class="card-text" style="min-height: 80px;">'+data[i].bookName+'</p>'+
                '</div>'+
                '</div>'+
                '</div>'+
                '<input type="hidden" id="custId" name="custId" value="'+ data[i].id+'">');
                
            }
            var trendingbook =$('#trending-book');
            $(trendingbook).empty();
            for (i=30; i<36 ;i++){
                $(trendingbook).append(' <div class="col-md-2">' + 
                '<div class="card " style="width: 172px ; height: 294px; border: none;">'+
                '  <img onclick="Bookdetail('+data[i].id+')" id="book-detailss"  src=" '+ data[i].imgBookM + ' " class="card-img-top card-img-book" alt="the boss">'+
                ' <div class="card-body " >'+
                '<p class="card-text" style="min-height: 80px;">'+data[i].bookName+'</p>'+
                '</div>'+
                '</div>'+
                '</div>'+
                '<input type="hidden" id="custId" name="custId" value="'+ data[i].id+'">');
                
               
            }
            var topcatetory =$('#top-caetory');
            $(topcatetory).empty();
            for (i=20; i<26 ;i++){
                $(topcatetory).append(' <div class="col-md-2">' + 
                '<div class="card " style="width: 172px ; height: 294px; border: none;">'+
                '  <img onclick="Bookdetail('+data[i].id+')" id="book-detailss"  src=" '+ data[i].imgBookM + ' " class="card-img-top card-img-book" alt="the boss">'+
                ' <div class="card-body " >'+
                ' <p class="card-text" style="min-height: 80px;">'+data[i].bookName+'</p>'+
                '</div>'+
                '</div>'+
                '</div>'+
                '<input type="hidden" id="custId" name="custId" value="'+ data[i].id+'">');
                
                
            }
           
        }
    }
    );
});

function Bookdetail(bookid){
   
    window.location='http://127.0.0.1:8000/detail-book/?id='+bookid;
   
}

// $( document ).ready(function() {
    
// })

