$(function(){
	//加减发送ajax
	function doajax(goodsid,gnum){
		$.ajax({
		    url:'/cartgchan',//当前请求的url地址
		    type:'get',//当前请求的方式 get  post
		    data:{'goodsid':goodsid,'goodsnum':gnum},//请求时发送的参数
		    dataType:'json',//返回的数据类型
		    error:function(){
		        //ajax执行失败后执行的代码
		        alert('ajax执行错误');
		    },
		})
	}
	//加号
	$('.cartshow .jia').click(function() {
		var gnum = $(this).next('span').text();
		var store = $(this).next('span').attr('value');
		if(gnum!=store){
			gnum++;
			$(this).next('span').text(gnum);
			price = Number($(this).parent().prev('td').text());
			total = price * gnum
			$(this).parent().next('td').text(total)
			$(this).next('span').next('input').removeAttr('disabled');
			var goodsid=$(this).parent().next('td').next('td').find('span').attr('value')
			doajax(goodsid,gnum)
			if($(this).parents('tr').find(".checkgoods").find("input").is(":checked")){
				var totalprice = Number($('.totalprice').find('span').find('span').text());
				totalprice += price;
				$('.totalprice').find('span').find('span').text(totalprice)
			}
		}
		else{
			alert('超出库存!')
			$(this).attr({
				disabled: 'disabled'
			});
		}
		
	});
	//减号
	$('.cartshow .jian').click(function() {
		var gnum = $(this).prev('span').text();
		if(gnum!=1){
			gnum--;
			$(this).prev('span').text(gnum);
			price = Number($(this).parent().prev('td').text());
			total = price * gnum
			$(this).parent().next('td').text(total)
			$(this).prev('span').prev('input').removeAttr('disabled');
			var goodsid=$(this).parent().next('td').next('td').find('span').attr('value')
			doajax(goodsid,gnum)
			if($(this).parents('tr').find(".checkgoods").find("input").is(":checked")){
			var totalprice = Number($('.totalprice').find('span').find('span').text());
			totalprice -= price;
			$('.totalprice').find('span').find('span').text(totalprice)
		}
		}
		else{
			$(this).attr({
				disabled: 'disabled'
			});
		}
	});
	//×号
	$('.cartshow table .gdel').click(function(){
		var flag= confirm('确定删除?')
		if(flag){
			var goodsid=$(this).find('span').attr('value')
			$.ajax({
			    url:'/cartgdel',//当前请求的url地址
			    type:'get',//当前请求的方式 get  post
			    data:{'goodsid':goodsid},//请求时发送的参数
			    dataType:'json',//返回的数据类型
			    success:function(data){
			        if(data.data){
			        	alert('删除成功');
			        }
			        else{
			        	alert('删除失败');
			        }
			        location.reload();
			    },
			    error:function(){
			        //ajax执行失败后执行的代码
			        alert('ajax执行错误');
			    },
			})
		}
	});
	//全选反选
	$('.choice .choice1').click(function() {
		var checkbox=$('input[name=chiocegoods]') //获取所有多选框
		flag = $(this).attr("flag");
		var total = 0;
		var totalnum = Number($('.totalnum').text());
		if(flag=='1'){
			for(i in checkbox.get()){
				checkbox.get(i).checked=true;
				total+=Number($(checkbox.get(i)).parent().siblings('.xiaoji').text());
			}
			i++;
			$('.totalnum').text(i);
			$(this).attr("flag",0);
			$(this).text("全不选");
		}
		else{
			for(i in checkbox.get()){
				checkbox.get(i).checked=false;
			}
			$('.totalnum').text(0);
			$(this).attr("flag",1);
			$(this).text("全选");
		}
		$('.totalprice').find('span').find('span').text(total);
	});

	//清空
	$('.choice .clear').click(function() {
		//判断购物车是否已经为空
		var element = $('.cartinfo').find('td').get();
		if(jQuery.isEmptyObject(element)){
			return;
		}
		//不为空则删除
		var flag = confirm("确定清空?");
		if(!flag){
			return false;
		}
		else{
			$.ajax({
			    url:'/cartclaer',//当前请求的url地址
			    type:'get',//当前请求的方式 get  post
			    dataType:'json',//返回的数据类型
			    success:function(data){
			        location.reload();
			    },
			    error:function(){
			        //ajax执行失败后执行的代码
			        alert('ajax执行错误');
			    },
			})
		}
	});

	//总计
	$('input[name=chiocegoods]').change(function() {
		var state = $(this).is(":checked");
		var xiaoji = Number($(this).parent().siblings('.xiaoji').text());
		var totalprice = Number($('.totalprice').find('span').find('span').text());
		var totalnum = Number($('.totalnum').text());
		if(state){
			totalprice += xiaoji;
			totalnum ++;
		}
		else{
			totalprice -= xiaoji;
			totalnum --;
		}
		$('.totalnum').text(totalnum);
		$('.totalprice').find('span').find('span').text(totalprice);
	});
	//表单提交事件
	$('.cartshow form').submit(function() {
		var checkbox=$('input[name=chiocegoods]');
		for(i in checkbox.get()){
			if(checkbox.get(i).checked){
				return true;
			}
		}
		return false;
	});
});