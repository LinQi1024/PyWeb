$(function(){
	//标记格式是否都正确
	flag = new Array();
	flag['pass1'] = false;
	flag['pass2'] = false;

	//判断第一个密码
	$('input[name=passwd]').focus(function(){
		$(this).next('span').html('')
	});
	$('input[name=passwd]').blur(function(){
		pass = $(this).val();
		if(pass.length<6){
			$(this).next('span').html('密码不能低于六位');
			flag['pass1'] = false;
		}
		else{
			flag['pass1'] = true;
		}
	});

	//邮编格式判断
	$('input[name=passwd2]').focus(function(){
		$(this).next('span').html('')
	});
	$('input[name=passwd2]').blur(function(){
		pass2 = $(this).val();
		pass1 = $('input[name=passwd]').val();
		if(pass2!=pass1){
			$(this).next('span').html('两次密码不一致');
			flag['pass2'] = false;
		}
		else{
			flag['pass2'] = true;
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