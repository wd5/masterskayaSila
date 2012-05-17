$(function() {

    $('.load_items').live('click',function(){
        var el = $(this);
        var parent = $(this).parent();
        $.ajax({
            url: "/load_items/",
            data: {
                cnt: el.find('.cnt').html(),
                init_cnt: parent.find('.init_cnt').val(),
                m_name: parent.find('.m_name').val(),
                a_name: parent.find('.a_name').val()
            },
            type: "POST",
            success: function(data) {

                parent.append(data)
                parent.find('.loaded').fadeIn('slow')
                parent.find('div').removeClass('loaded')
                parent.find('a.load_items').appendTo(parent)
                parent.find('.init_cnt').val(parent.find('#endrange').val())
                parent.find('#endrange').remove()
                var rctxt = parent.find('#remaining_count_text').val()
                var rc = parent.find('#remaining_count').val()
                if (rctxt!=undefined)
                    {el.html(rctxt)}

                if (rc==0)
                    {el.remove()}

                parent.find('#remaining_count_text').remove()
                parent.find('#remaining_count').remove()
            }
        });

        return false;
    });


});