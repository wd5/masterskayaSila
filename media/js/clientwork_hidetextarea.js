$(function() {
    $('td.code_video').find('textarea').hide()
    $('td.workcategory').find('select option[value="4"][selected="selected"]').parent().parent().parent().find('textarea').css({'width':'150px','height':'50px'}).show()
    $('td.workcategory').live('change',function(){
        if ($(this).find('select option:selected').val()==4)
            {$(this).parent().find('td.code_video textarea').css({'width':'150px','height':'50px'}).show()}
        else
            {$(this).parent().find('td.code_video textarea').val('')
            $(this).parent().find('td.code_video textarea').hide()}
    });
});