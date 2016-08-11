function autoscroll () {
    $(document).ready(function(){
    $('#msg_list').animate({
    scrollTop: $('#msg_list').get(0).scrollHeight}, 1);
});};

$('#chat-form').on('submit', function (event) {
    event.preventDefault();


     $.ajax({
        url: '/process_msg/',
        type: 'POST',
        data: {'new_msg': $('#new_msg').val()},

        success: function (json) {
            autoscroll();
            //location.reload();
            $('#new_msg').val('');
            $('#msg_list').val('');
            $('#msg_list').html(json['messages']);
            autoscroll();
        }
    })
});

function getNewMessages() {
    $.get('/get_messagesJSON/', function (json) {
        $('#msg_list').html(json['messages']);
        autoscroll();
    })
}

refreshTimer = setInterval(getNewMessages, 2000);



// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

autoscroll();
var csrftoken = getCookie('csrftoken');