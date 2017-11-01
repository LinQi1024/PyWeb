$(function(){
	//订单确定提交后
	$('.confirm-btn').click(function() {
		$.ajax({
		    url:'/ordersure',//当前请求的url地址
		    type:'get',//当前请求的方式 get  post
		    dataType:'json',//返回的数据类型
		    success:function(data){
		    	if (data.info == true){
		    		info = "订单提交成功!"
		    	}
		    	else{
		    		info = "订单提交失败,库存超出!"
		    	}
		    	alert(info)
		    	window.location.href="/cartshow";
		    	
		    },
		    error:function(){
		        //ajax执行失败后执行的代码
		        alert('ajax执行错误');
		    },
		})
		
	});
});