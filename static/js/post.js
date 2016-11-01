$(document).ready(function() {
	function resizePostImg() {
		var postWidth = $('.post').width();
		style = {
			'width': postWidth + 'px',
			'margin-left': '-30px'
		}
		$('.post-content').find('img').css(style);
	}

	resizePostImg();

	$(window).resize(function() {
        resizePostImg();
    });
});