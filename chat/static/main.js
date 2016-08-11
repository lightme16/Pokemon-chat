function autoscroll () {
    $(document).ready(function(){
    $('#msg_list').animate({
    scrollTop: $('#msg_list').get(0).scrollHeight}, 1);
});};

autoscroll()

$('#send_text').on('click',function () {
    $.ajax({
        url: '/proccess_msg/',
        type: 'POST',
        data: {'msg_text': $('#msg_text').val()},

        success: function (json) {
            $("#msg_text").val('')
            autoscroll();
            location.reload();
        }
    })
});

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
var csrftoken = getCookie('csrftoken');

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