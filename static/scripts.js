$(function () {
    setInterval(function () {
        $.ajax({
            url: '/test',
            type: 'POST',
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            data: JSON.stringify({
                payload: Math.floor(Date.now() / 1000)
            }),
            success: function(response) {
                footer_aside_content = $('footer > aside > div.content');
                for (let i in response) {
                    footer_aside_content.prepend(response[i] + '<br />').scrollTop(0)
                }
            }
        });
    }, 333)
});
