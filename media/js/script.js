$(function(){

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
    SetJcoverFlip();
});

function SetJcoverFlip()
{
    $('.flip').jcoverflip({
        current: 1,
        titleAnimateIn: function(s){},
        titleAnimateOut: function(){},
        beforeCss: function( el, container, offset ){
            return [
                $.jcoverflip.animationElement( el, { left: (-150*offset+15)+'px', top: '180px' }, { } ),
                $.jcoverflip.animationElement( el.find( 'img' ), { opacity: Math.max(0.1,0.4-0.4*offset), width: Math.max(10,100-100*offset)+'px' }, {} )
            ];
        },
        afterCss: function( el, container, offset ){
            return [
                $.jcoverflip.animationElement( el, { left: (620*(offset+1))+'px', top: (70+70*offset)+'px' }, { } ),
                $.jcoverflip.animationElement( el.find( 'img' ), { opacity: Math.max(0.1,0.7-0.7*offset), width: Math.max(10, 310-100*offset)+'px' }, {} )
            ];
        },
        currentCss: function( el, container ){
            return [
                $.jcoverflip.animationElement( el, { left: '145px', top: '0px' }, { } ),
                $.jcoverflip.animationElement( el.find( 'img' ), { opacity: 1, width: '401px' }, { } )
            ];
        }
    });

    $('.ui-jcoverflip--item img').hover(function(){
        opct = $(this).css('opacity');
        $(this).css('opacity',1);
    },
    function(){
        $(this).css('opacity',opct);
    });
    $('.ui-jcoverflip--item img').click(function(){
        $(this).css('opacity',1);
        opct = 1;
    })
}