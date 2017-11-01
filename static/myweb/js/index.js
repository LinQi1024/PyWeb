$(function(){
	
	//热门商品按钮
	$('.pan-hot-body .row div').hover(function(){
		$(this).find('.hot-p3').hide()
		$(this).find('.hot-btn').show()
	},function(){
		$(this).find('.hot-btn').hide()
		$(this).find('.hot-p3').show()
	});
	//end 热门商品按钮

})