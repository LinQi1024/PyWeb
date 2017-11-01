$(function(){
	//标记格式是否都正确
	flag = new Array();
	flag['passwd'] = true;
	flag['passwd2'] = true;
	flag['code'] = true;
	flag['phone'] = true;
	flag['email'] = true;

	//手机正则
	var regP = /^1[3,5,8]\d{9}$/;
	//邮箱正则
	var regE = /^\w+@\w+[.]\w+$/;

	//密码判断
	$('input[name=passwd]').focus(function(){
		$(this).next('span').html('');
	});

	$('input[name=passwd]').blur(function(){
		passwd = $(this).val();
		if(passwd==''){
			$(this).next('span').html('密码不能为空');
			flag['passwd'] = false;
		}
		else if(passwd.length < 6 | passwd.length > 18){
			$(this).next('span').html('密码格式错误');
			flag['passwd'] = false;
		}
		else{
			flag['passwd'] = true;
		}
	});

	//第二次输入密码判断
	$('input[name=passwd2]').focus(function(){
		$(this).next('span').html('');
	});

	$('input[name=passwd2]').blur(function(){
		passwd2 = $(this).val();
		if(passwd2!=$('input[name=passwd]').val()){
			$(this).next('span').html('两次密码不一致');
			flag['passwd2'] = false;
		}
		else{
			flag['passwd2'] = true;
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
		if(email==''){
			$(this).next('span').html('邮箱不能为空');
			flag['email'] = false;
		}
		else if(!res){
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