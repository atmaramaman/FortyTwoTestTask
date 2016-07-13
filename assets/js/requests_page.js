setInterval(function() {
            $.ajax({
                url: REQUESTS_PAGE_URL,
                type: 'GET',
                dataType: 'json',
                success: function(data) {
                    $('#ajax_requests').html('');
                    for (index in data.request) {
                        var text = data.request[index];
                        $('#ajax_requests').append('<p>' + text);
                    }
                }
            });
          }, 1000);