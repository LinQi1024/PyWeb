$(function(){
	var val;
	$('.statusedit').click(function() {
		var zhuangtai = $(this).parent().prev('td').children('span').text();
		if(zhuangtai == '新订单'){
			$('.status').find('input:eq(0)').attr({'disabled':'disabled'})
			$('.status').find('input:eq(2)').attr({'disabled':'disabled'})
		}
		else if(zhuangtai == '已发货'){
			$('.status').find('input:eq(0)').attr({'disabled':'disabled'})
			$('.status').find('input:eq(1)').attr({'disabled':'disabled'})
			$('.status').find('input:eq(3)').attr({'disabled':'disabled'})
		}
		else{
			$('.status').find('input:eq(0)').attr({'disabled':'disabled'})
			$('.status').find('input:eq(1)').attr({'disabled':'disabled'})
			$('.status').find('input:eq(2)').attr({'disabled':'disabled'})
			$('.status').find('input:eq(3)').attr({'disabled':'disabled'})
		}
		$('.status').slideDown();
		val = $(this).parent().siblings().first().text();
		return false;
	});
	$('.status button').click(function() {
		var val1 = $('.status input[type="radio"]:checked').val();
		$.ajax({
	    	url:'/myadmin/ordersupdate',//当前请求的url地址
	    	type:'get',//当前请求的方式 get  post
	    	data:{orderid:val,option:val1},//请求时发送的参数
	    	dataType:'json',//返回的数据类型
	    	success:function(data){
	        	//ajax请求成功后执行的代码
	        	if (data.data){
	        		alert('修改成功');
	        	 	location.reload();
	        	}
	        	else{
	        		alert("修改失败")
	        	}
	    	},
	    	error:function(){
	        	//ajax执行失败后执行的代码
	        	alert('执行错误');
	   		},
		})
	});
})