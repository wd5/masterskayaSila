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
});