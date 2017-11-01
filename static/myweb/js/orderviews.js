$(function(){
	//点击查看事件
	$('tbody .odetail').click(function() {
		var domthis=$(this)
		var	orderid=$(this).attr('orderid');
		var content=$(this).text();
		if(content=="查看"){
			$.ajax({
			    url:'/orderdetail',//当前请求的url地址
			    type:'get',//当前请求的方式 get  post
			    data:{'orderid':orderid},
			    dataType:'json',//返回的数据类型
			    success:function(data){
			    	shoplist = data['shoplist']
			    	for(shop in shoplist){
			    		var tr = $("<tr name='"+orderid+"'style='border:1px solid #c0c0c0;'></tr>")
			    		$("<td></td>").appendTo(tr)
			    		$("<td>"+data.shoplist[shop]['goodsid']+"</td>").appendTo(tr)
			    		$("<td><img src='static/imgs/goods/"+data.shoplist[shop]['picname']+"'></td>").appendTo(tr)
			    		$("<td>"+data.shoplist[shop]['name']+"</td>").appendTo(tr)
			    		$("<td>"+data.shoplist[shop]['price']+"</td>").appendTo(tr)
			    		$("<td>"+data.shoplist[shop]['num']+"</td>").appendTo(tr)
			    		$("<td></td>").appendTo(tr)
			    		$("<td></td>").appendTo(tr)
			    		$("<td></td>").appendTo(tr)
			    		domthis.parents('tr').after(tr)
			    	}
			    	domthis.parents('tr').after("<tr name='"+orderid+"'style='border:1px solid #c0c0c0;'><th></th><th>商品编号</th><th>图片</th><th>名称</th><th>价格</th><th>数量</th><th></th><th></th><th></th></tr>")
			    	domthis.text('关闭')
			    	
			    },
			    error:function(){
			        //ajax执行失败后执行的代码
			        alert('ajax执行错误');
			    },
			})
		}
		else{
			$(this).parents('tr').nextAll("tr[name='"+orderid+"']").remove();
			$(this).text('查看');
		}
		
	});
	//点击取消事件
	$('tbody .ocancel').click(function() {
		var flag = confirm('确定取消订单?');
		if(!flag){
			return false;
		}
		else{
			var oid = $(this).attr('orderid');
			$.ajax({
			    url:'/ordercancel',//当前请求的url地址
			    type:'get',//当前请求的方式 get  post
			    data:{'orderid':oid},
			    dataType:'json',//返回的数据类型
			    success:function(data){
			    	if(data.info){
			    		alert('已取消');
			    	}
			    	else{
			    		alert('取消失败')
			    	}
			    	location.reload();
			    },
			    error:function(){
			        //ajax执行失败后执行的代码
			        alert('ajax执行错误');
			    },
			});
		}
	});
})