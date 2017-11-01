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

	//客服图标
	$('.pan-kefu-body a').hover(function(){
		$('.pan-kefu-img').attr('src','/static/myweb/imgs/kefu-active.png')
	},function(){
		$('.pan-kefu-img').attr('src','/static/myweb/imgs/kefu.png')
	});
	// end客服图标

})