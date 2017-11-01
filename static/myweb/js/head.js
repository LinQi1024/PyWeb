$(function(){
	/*导航1右侧的两个图标*/
	$('.nav1 .nav1-right li:eq(0)').hover(function(){
		$(this).find('img').attr('src','/static/myweb/imgs/user-active.png')
	},function(){
		$(this).find('img').attr('src','/static/myweb/imgs/user.png')
	});
	$('.nav1 .nav1-right li:eq(1)').hover(function(){
		$(this).find('img').attr('src','/static/myweb/imgs/cart-active.png')
		//导航栏购物车内容显示
		$.ajax({
		    url:'/cartshow',//当前请求的url地址
		    type:'get',//当前请求的方式 get  post
		    dataType:'json',//返回的数据类型
		    success:function(data){
		    	shops = data.shoplist
		    	if(!($.isEmptyObject(shops))){
		    		$('.cart-dis').children('img').nextAll().remove();
		    		var table = $("<table style='position:absolute;top:10px;width:100%;'></talbe>")
		    		for(shop in shops){
		    			var tr = $("<tr></tr>")
		    			$("<td style='border:1px solid #ccc;width:30%'>"+shops[shop].goods+"</td>").appendTo(tr);
		    			$("<td style='border:1px solid #ccc;width:10%'><img src='static/imgs/goods/"+shops[shop].picname+"' width='80px;'></td>").appendTo(tr);
		    			$("<td style='border:1px solid #ccc;width:30%'>"+'￥ '+shops[shop].price+"</td>").appendTo(tr);
		    			$("<td style='border:1px solid #ccc;width:20%'>"+shops[shop].gnum+"</td>").appendTo(tr);
		    			tr.appendTo(table);
		    		}
		    		table.appendTo($('.cart-dis'));
		    	}
		    },
		    error:function(){
		        //ajax执行失败后执行的代码
		        //alert('ajax执行错误');
		    },
		    timeout:2000,//设置当前请求的超时时间  毫秒,必须时异步请求才会生效
    		async:false// 是否异步  true为异步  false 同步
		});
		$('.cart-dis').fadeIn();
	},function(){
		$(this).find('img').attr('src','/static/myweb/imgs/cart.png');
		$('.cart-dis').hide();
	});
	/*end 导航1右侧的两个图标*/

	/*导航1右侧的购物车图标显示*/
	$('.cart-dis').hover(function(){
		$(this).show();
	},function(){
		$(this).hide();
	})
	/*end 导航1右侧的购物车图标显示*/

	/*导航1固定在顶部*/
	$(window).scroll(function(){
		//获取屏幕宽度
		var winwidth=$(window).width();
		// 当为PC端的时候
		if(winwidth>=1300){
			var scrTop = $(document).scrollTop();
			if(scrTop>=400){
				$('.nav1').css({
					'position':'fixed',
					'top':0,
					'z-index': 20,
					'width':'100%',
					'min-height':'50px'
				});
				$('.nav1-con').css({
					'margin-top':0
				});
				$('.logout').css({
					'position':'absolute',
					'right':'40px',
					'top':'20px'
				});
			}
			else{
				$('.nav1').css({
					'position':'relative',
					'min-height':'100px'
				})
				$('.nav1-con').css({
					'margin-top':'20px'
				});
				$('.logout').css({
					'position':'absolute',
					'right':'40px',
					'top':'40px'
				});
			}
		}//当为移动端的时候
		else{
			var scrTop = $(document).scrollTop();
			if(scrTop>=400){
				$('.nav1').css({
					'position':'fixed',
					'top':0,
					'z-index': 20,
					'width':'100%'
				});
			}
			else{
				$('.nav1').css({
					'position':'relative'
				})
			}
		}
		
	});
	/* end 导航1固定在顶部*/

	//导航2手机
	$('.nav2 .phone').hover(function(){
		$('.phone-dis').slideDown();
	},function(){
		$('.phone-dis').hide();
	}) 
	$('.phone-dis').hover(function(){
		$(this).show();
	},function(){
		$(this).slideUp();
	})
	//end导航2手机 

	//back-top
	$(window).scroll(function(){
		var scroTop = $(document).scrollTop();
		if(scroTop>=600){
			$('.back-top').css({
				bottom:'30px'
			})
		}
		else{
			$('.back-top').css({
				bottom:'-30px'
			})
		}
	});
	$('.back-top').click(function(){
		$('body').animate({
			scrollTop:'0px'
		});
	});
	//end back-top
})