var count = 0;
setInterval(function() {
            $.ajax({
                url: REQUESTS_PAGE_URL,
                type: 'GET',
                dataType: 'json',
                success: function(data) {
                    var last_request = $('#ajax_requests').children().first().html();

                    if (data.request != last_request) {
                        count = count + 1;
                        $('title').text(count);
                        $('#ajax_requests').prepend('<p>' + data.request);
                        var count_req = $('#ajax_requests p').length;
                        if (count_req === 11) {
                            $('#ajax_requests').children().last().remove();
                        }
                    }
                }
            });
          }, 1000);
$(document).ready(function() {
    $('#ajax_requests').mouseover(function () {
        $('p').css('color', 'grey');
        $('title').text(0);
        count = 0;
    });
});