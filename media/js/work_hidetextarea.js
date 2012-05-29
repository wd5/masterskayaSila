$(function() {
    $('td.code_video').find('textarea').hide()
    id_cat = $('#id_workcategory').find('option[selected="selected"]').attr('value')
    if (id_cat == 4)
        {$('td.code_video').find('textarea').css({'width':'150px','height':'50px'}).show()}

    $('#id_workcategory').live('change',function(){
        if ($(this).find('option:selected').attr('value') == 4)
            {$('td.code_video').find('textarea').css({'width':'150px','height':'50px'}).show()}
        else
            {$('td.code_video').find('textarea').hide()}
    });
});