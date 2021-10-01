$(function()
{
    var running = false,
        delay = 128,
        button_start = $('header nav .buttons button#start'),
        button_pause = $('header nav .buttons button#pause'),
        button_restart = $('header nav .buttons button#restart'),
        aside_aside = $('#aside > aside'),
        header_nav_blockchain_length = $('header nav #blockchain_length'),
        header_nav_total_transactions = $('header nav #total_transactions'),
        section_content = $('section#content'),
        footer_aside_content = $('footer > aside > div.content'),
        interval_ajax_update_aside_aside =
        interval_ajax_update_header_nav_blockchain_length =
        interval_ajax_update_section_content =
        interval_ajax_update_footer_aside_content = null;

    bootstrap()

    function button_start_click()
    {
        button_start.hide();
        button_pause.show();
        running = true;
        bootstrap();
    }
    button_start.on('click', button_start_click);

    function button_pause_click(then)
    {
        button_pause.hide();
        if (then == 'restart') {
            button_restart.show();
        } else {
            button_start.show();
        }
        running = false;
        bootstrap();
    }
    button_pause.on('click', button_pause_click);

    function button_restart_click()
    {
        window.location.href = '/restart';
    }
    button_restart.on('click', button_restart_click);

    function update_aside_aside(response)
    {
        aside_aside.empty()
        if (response.length <= 1)
            button_pause_click(); // button_pause_click('restart');
        for (let i in response) {
            html = '<div class="content relative">'
                 + '    <span style="color:' + response[i].color + '">' + response[i].name + ' (' + response[i].auto_behaviour.toUpperCase() + ')</span>'
                 + '    <span style="float:right">(' + response[i].tokens.toFixed(5) + ' ' + response[i].token_iso + ')</span>'
                 + '    <hr />'
                 + '    <span class="player" style="align-items:center;display:flex;font-size:.5em;justify-content:space-between">'
                 + '        <span><strong>Entropy: ' + response[i].entropy + '</strong></span>'
                 + '        <span>|</span>'
                 + '        <span>Attack: ' + response[i].attack
                 + '        ' + ((Math.pow(response[i].attack, 2) <= response[i].tokens)
                                ? '<a href="JavaScript:;" class="power_up">+</a>'
                                : '')
                 + '        </span>'
                 + '        <span>Defence: ' + response[i].defence
                 + '        ' + ((Math.pow(response[i].attack, 2) <= response[i].tokens)
                                ? '<a href="JavaScript:;" class="power_up">+</a>'
                                : '')
                 + '        </span>'
                 + '        <span>Speed: ' + response[i].speed
                 + '        ' + ((Math.pow(response[i].speed, 2) <= response[i].tokens)
                                ? '<a href="JavaScript:;" class="power_up">+</a>'
                                : '')
                 + '        </span>'
                 + '    </span>'
                 + '</div>';
            aside_aside.append(html);
        }
        $.ajax({
            url: '/node/get',
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                for (let i in response) {
                    html = '<div class="content relative npc">'
                         + '    ' + response[i].id
                         + '    <span style="float:right">(' + response[i].tokens.toFixed(5) + ' ' + response[i].token_iso + ')</span>'
                         + '</div>';
                    aside_aside.append(html);
                }
                aside_aside.append('<div id="death_broom"></div>');
            }
        });
    }

    function ajax_update_aside_aside()
    {
        $.ajax({
            url: '/player/get',
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                update_aside_aside(response)
            }
        });
    }
    //ajax_update_aside_aside(); // DBG

    function ajax_update_header_nav_blockchain_length()
    {
        $.ajax({
            url: '/blockchain/get/length',
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                header_nav_blockchain_length.text(response.blockchain_length)
                header_nav_total_transactions.text(response.total_transactions)
            }
        });
    }
    ajax_update_header_nav_blockchain_length(); // always at startup (beacause of genesis block)

    function update_section_content(response)
    {
        section_content.empty()
        $.each(response, function(key, data) {
            html = '<span class="node" style="'
                    + 'background-color:' + data.color + ';'
                    + 'box-shadow: 0 0 ' + (data.entropy + data.tokens) + 'px ' + data.color + ';'
                    + 'height:' + (data.entropy + data.tokens / 4) + '%;'
                    + 'left:' + data.pos_x + '%;'
                    + 'top:' + data.pos_y + '%;'
                    + 'width:' + (data.entropy + data.tokens / 4) + '%"'
                    + '>&nbsp;</span>'
            section_content.append(html)
        });
    }

    function ajax_update_section_content()
    {
        $.ajax({
            url: '/status/get',
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                update_section_content(response)
            }
        });
    }
    //ajax_update_section_content(); // DBG

    function update_footer_aside_content(response)
    {
        footer_aside_content.empty()
        for (let i in response) {
            footer_aside_content.prepend(response[i] + '<br />').scrollTop(0)
        }
    }

    function ajax_update_footer_aside_content()
    {
        $.ajax({
            url: '/log/get',
            type: 'GET',
            dataType: 'json',
            //contentType: 'application/json; charset=utf-8',
            //data: JSON.stringify({
            //    payload: Math.floor(Date.now() / 1000)
            //}),
            success: function(response) {
                update_footer_aside_content(response)
            }
        });
    }
    ajax_update_footer_aside_content(); // always at startup (because of init logging)

    function bootstrap()
    {
        if (running) {
            interval_ajax_update_aside_aside = setInterval(ajax_update_aside_aside, delay * 60);
            interval_ajax_update_header_nav_blockchain_length = setInterval(ajax_update_header_nav_blockchain_length, delay);
            interval_ajax_update_section_content = setInterval(ajax_update_section_content, delay);
            interval_ajax_update_footer_aside_content = setInterval(ajax_update_footer_aside_content, delay * 6);
        } else {
            clearInterval(interval_ajax_update_aside_aside);
            clearInterval(interval_ajax_update_header_nav_blockchain_length);
            clearInterval(interval_ajax_update_section_content);
            clearInterval(interval_ajax_update_footer_aside_content);
        }
    }

    if (window.index) {
        ajax_update_section_content();
    } else {
        ajax_update_aside_aside();
    }
});
