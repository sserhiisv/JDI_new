$(document).ready(function() {
	function resizePostTitle() {
		var postWidth = $('.main-post-inner-desc').width();
		var popularPostWidth = $('.right-popular').width();
		var randomRecomendWidth = $('.f-read-block').width();


		$('.main').find('.main-post-inner-desc').css('height', 0.5625 * postWidth + 'px');
		$('.main').find('.main-post-inner').css('height', 0.5625 * postWidth + 'px');

		$('.right-popular').find('.right-popular-inner').css('height', 0.5625 * popularPostWidth + 'px');

		$('.f-read-set').find('.f-read-block').css('height', 0.5625 * randomRecomendWidth + 'px');
		$('.f-read-set').find('.f-read-block-img').css('height', 0.5625 * randomRecomendWidth + 'px');

	}

	resizePostTitle();

	$(window).resize(function() {
        resizePostTitle();
    });
});