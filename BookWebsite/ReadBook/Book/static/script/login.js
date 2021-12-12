

$('#form_login').on('submit', function(e) {
    var username = $('#username').val().trim();
    var password = $('#password').val().trim();
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/api/oauth2-info/',
        success: function (data) {
          
           window.localStorage.setItem('client_id',data.client_id);
           window.localStorage.setItem('client_secret',data.client_serect);
          
        }
    }
    );
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/o/token/',
        data:{
            'username':username,
            'password':password,
            'client_id':window.localStorage.getItem('client_id'),
            'client_secret':window.localStorage.getItem('client_secret'),
            'grant_type':'password'
        },
        success: function (data) {
            window.localStorage.setItem('access_token',data.access_token);
        }
    });
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/api/user/current-user/',
        headers :{
            'Authorization' : `Bearer ${window.localStorage.getItem('access_token')}`
        },
        success: function (data) {
           
            window.localStorage.setItem('username',data.username);
            window.localStorage.setItem('idusername',data.id);
        }
    }),
   
    window.location= "http://127.0.0.1:8000/home";
})



