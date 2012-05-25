$(function(){

	function overflow() {
		if ($('body').width() < 996) {
			$('body').css('overflow-x','visible');
			$('.page').css('overflow-x','hidden');
		} else {
			$('body').css('overflow-x','hidden');
			$('.page').css('overflow-x','visible');
		}
	}
	$('#login_lnk').click(function(){
		$('.overlay').show();
		return false;
	});
	$('.ic_close').click(function(){
		$(this).parent().parent().parent().hide();
	});
	$(window).resize(function(){
		overflow();
	});
	overflow();

    // для блока block_adv_maintenance 'small'
    p = $('#adv_text_blc').find('p').first();
    $('#adv_text_blc').html($('#adv_text_blc').find('a'));
    $('#adv_text_blc').prepend(p);
    $('#adv_text_blc').show();

    $('.fancybox').fancybox();



    $(".play_ic, .play_ic_zs").live('click',function(){
        $.fancybox({
                'padding'		: 0,
                'autoScale'		: false,
                'transitionIn'	: 'none',
                'transitionOut'	: 'none',
                'title'			: this.title,
                'width'		    : 680,
                'height'		: 495,
                'href'			: this.href.replace(new RegExp("watch\\?v=", "i"), 'v/'),
                'type'			: 'swf',
                'swf'			: {
                     'wmode'		: 'transparent',
                    'allowfullscreen'	: 'true'
                }
            });

        return false;
    });



});
