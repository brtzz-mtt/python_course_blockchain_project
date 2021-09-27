$(function()
{
    aside_aside = $('#aside > aside');

    setInterval(function () {
        $.ajax({
            url: '/player/get',
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                aside_aside.empty()
                for (let i in response) {
                    aside_aside.append('<div class="content relative"><span style="color:' + response[i].color + '">' + response[i].name + '</span> <span style="float:right">(' + response[i].tokens.toFixed(3) + ')</span></div>')
                }
                $.ajax({
                    url: '/node/get',
                    type: 'GET',
                    dataType: 'json',
                    success: function(response) {
                        console.log(response)
                        for (let i in response) {
                            aside_aside.append('<div class="content relative npc">' + response[i].id + ' <span style="float:right">(' + response[i].tokens.toFixed(3) + ')</span></div>')
                        }
                    }
                });
            }
        });
    }, 6666);

    footer_aside_content = $('footer > aside > div.content');

    setInterval(function () {
        $.ajax({
            url: '/log/get',
            type: 'GET',
            dataType: 'json',
            //contentType: 'application/json; charset=utf-8',
            //data: JSON.stringify({
            //    payload: Math.floor(Date.now() / 1000)
            //}),
            success: function(response) {
                for (let i in response) {
                    footer_aside_content.prepend(response[i] + '<br />').scrollTop(0)
                }
            }
        });
    }, 3333); // updates content every 10 second(s)
});
