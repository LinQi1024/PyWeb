$(function(){
	//标记格式是否都正确
	flag = new Array();
	flag['name'] = true;
	flag['code'] = true;
	flag['phone'] = true;
	flag['email'] = true;

	//手机正则
	var regP = /^1[3,5,8]\d{9}$/;
	//邮箱正则
	var regE = /^\w+@\w+[.]\w+$/;

	//姓名判断
	$('input[name=name]').focus(function(){
		$(this).next('span').html('')
	});
	$('input[name=name]').blur(function(){
		code = $(this).val();
		if(code.length== ''){
			$(this).next('span').html('姓名不能为空');
			flag['name'] = false;
		}
		else{
			flag['name'] = true;
		}
	});

	//邮编格式判断
	$('input[name=code]').focus(function(){
		$(this).next('span').html('')
	});
	$('input[name=code]').blur(function(){
		code = $(this).val();
		if(code.length!=6){
			$(this).next('span').html('邮编格式错误');
			flag['code'] = false;
		}
		else{
			flag['code'] = true;
		}
	});

	//手机格式判断
	$('input[name=phone]').focus(function(){
		$(this).next('span').html('')
	});
	$('input[name=phone]').blur(function(){
		phone = $(this).val();
		var res=regP.test(phone);
		if(!res){
			$(this).next('span').html('手机格式错误');
			flag['phone'] = false;
		}
		else{
			flag['phone'] = true;
		}
	});

	//邮箱判断
	$('input[name=email]').focus(function(){
		$(this).next('span').html('')
	});
	$('input[name=email]').blur(function(){
		email = $(this).val();
		var res=regE.test(email);
		if(!res){
			$(this).next('span').html('邮箱格式错误');
			flag['email'] = false;
		}
		else{
			flag['email'] = true;
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