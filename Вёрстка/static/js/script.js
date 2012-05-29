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
	$('.flip').jcoverflip({
		current: 1,
		titleAnimateIn: function(){},
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
});