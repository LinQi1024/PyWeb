$(function(){
	//标记格式是否都正确
	flag = new Array();
	flag['name'] = true;
	flag['company'] = true;
	flag['descr'] = true;
	flag['imgfile'] = true;
	flag['price'] = true;
	flag['number'] = true;

	//商品名称为空判断
	$('input[name=name]').focus(function(){
		$(this).next('span').html('');
	});
	$('input[name=name]').blur(function(){
		username = $(this).val();
		if(username==''){
			$(this).next('span').html('商品名称不能为空');
			flag['name'] = false;
		}
		else{
			flag['name'] = true;
		}
	});

	//生产厂家为空判断
	$('input[name=company]').focus(function(){
		$(this).next('span').html('');
	});
	$('input[name=company]').blur(function(){
		username = $(this).val();
		if(username==''){
			$(this).next('span').html('生产厂家不能为空');
			flag['company'] = false;
		}
		else{
			flag['company'] = true;
		}
	});

	//简介为空判断
	$('textarea[name=descr]').focus(function(){
		$(this).next('span').html('');
	});
	$('textarea[name=descr]').blur(function(){
		username = $(this).val();
		if(username==''){
			$(this).next('span').html('简介不能为空');
			flag['descr'] = false;
		}
		else{
			flag['descr'] = true;
		}
	});

	//单价为空判断
	$('input[name=price]').focus(function(){
		$(this).next('span').html('');
	});
	$('input[name=price]').blur(function(){
		username = $(this).val();
		if(username==''){
			$(this).next('span').html('价格不能为空');
			flag['price'] = false;
		}
		else{
			flag['price'] = true;
		}
	});

	//库存量空判断
	$('input[name=number]').focus(function(){
		$(this).next('span').html('');
	});
	$('input[name=number]').blur(function(){
		username = $(this).val();
		if(username==''){
			$(this).next('span').html('库存数量不能为空');
			flag['number'] = false;
		}
		else{
			flag['number'] = true;
		}
	});

	//提交前确认格式是否都正确
	$('form').submit(function() {
		for(i in flag){
			if(flag[i]==false){
				alert('输入信息错误');
				return false;
			}
		}
	});
});