var count = 0;
var begin = 0;
var end = 0;
setInterval(function() {
            $.ajax({
                url: REQUESTS_PAGE_URL,
                type: 'GET',
                dataType: 'json',
                success: function(data) {
                    if (begin == 0) {
                        begin = data.count;
                    }
                    if (end == 0) {
                        end = data.count;
                    }
                    if (data.count > begin) {
                        end = data.count;
                    }
                    count = end - begin;
                    if (count > 0) {
                        $('title').text(count);
                        $('#ajax_requests').html('');
                        for (index in data.request) {
                            var text = data.request[index];
                            $('#ajax_requests').append('<p>' + text);
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
        begin = 0;
        end = 0;
    });
});