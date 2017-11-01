$(function(){

	//购买块左侧
	$('.pan-buy .buy-left-cont div').click(function(){
		$(this).css({
			border:'3px solid #ccc'
		}).siblings().css({
			border:'1px solid #F0F0F0'
		})
		var ind=$(this).index()+1;
		$('.pan-buy .buy-mid img').attr('src','/static/myweb/imgs/buy-b-'+ind+'.png');
	});
	//end 购买块左侧

	//购买右侧
	$('.buy-r-cho2 .jianBtn').click(function(){
		var num=$('.buy-r-cho2 .cho2-num').text();
		if(num!=1){
			num--;
			$('.buy-r-cho2 .cho2-num').text(num);
			$('input[name=goodsnum]').val(num);
		}
	});
	$('.buy-r-cho2 .jiaBtn').click(function(){
		var num=$('.buy-r-cho2 .cho2-num').text();
		if(num!=5){
			num++;
			$('.buy-r-cho2 .cho2-num').text(num);
			$('input[name=goodsnum]').val(num);
		}
	});
	//end 购买右侧

})