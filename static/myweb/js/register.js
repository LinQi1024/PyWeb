$(function(){
	//判断用户名是否规范
	var flag = new Array();
	flag['user']=false;
	flag['passwd1']=false;
	flag['passwd2']=false;
	flag['email']=false;
	var reg1 = /^1[3,5,8]\d{9}$/;
	var reg2 =/^\w+@\w+[.]\w+$/
	function panduan(){
		for(i in flag){
			if(!flag[i]){
				return;
			}
		}
		$('.login-btn button').removeAttr('disabled');
	}
	//用户名
	$('.login-user input').focus(function(){
		$('.login-warning').hide();
		$('.login-btn button').attr('disabled','disabled');
	});
	$('.login-user input').blur(function(){
		var userVal=$('.login-user input').val();
		if(userVal.length==0){
			flag['user']=false;
			return;
		}
		var res1=reg1.test(userVal);
		var res2=reg2.test(userVal);
		if(!(res1||res2)){
			$('.login-warning').show();
			flag['user']=false;
			return;
		}else{
			flag['user']=true;
			panduan()
		}
	});
	//密码
	$('.login-passwd input').focus(function() {
		$('.form-info').text(' ');
		$('.login-btn button').attr('disabled','disabled');
	});
	$('.login-passwd input').blur(function(){
		var passwdVal=$('.login-passwd input').val();
		if(passwdVal.length==0){
			flag['passwd1']=false;
			return;
		}
		if(passwdVal.length>=6){
			flag['passwd1']=true;
			if(passwdVal==$('input[name=passwd2]').val()){
				panduan()
			}
			else{
				$('.form-info').text('两次密码不一致');
			}
		}
		else{
			$('.form-info').text('密码格式错误');
			flag['passwd2']=false;
			return;
		}
	});
	//第二次密码
	$('input[name=passwd2]').focus(function() {
		$('.form-info').text(' ');
		$('.login-btn button').attr('disabled','disabled');
	});
	$('input[name=passwd2]').blur(function(){
		var passwdVal=$(this).val();
		if(passwdVal==$('.login-passwd input').val()){
			flag['passwd2']=true;
			panduan()
		}
		else{
			$('.form-info').text('两次密码不一致');
			flag['passwd2']=false;
			return;
		}
	});
	//email
	$('input[name=email]').focus(function() {
		$('.form-info').text(' ');
		$('.login-btn button').attr('disabled','disabled');
	});
	$('input[name=email]').blur(function(){
		var emialVal=$(this).val();
		var res2=reg2.test(emialVal);
		if(emialVal.length==0){
			flag['email']=false;
			return;
		}
		if(res2){
			flag['email']=true;
			panduan()
		}
		else{
			$('.form-info').text('邮箱格式错误');
			flag['email']=false;
			return;
		}
	});

	//end 判断用户名是否规范

	//尾部链接
	var srcimg='';
	$('.login-tail-l a').hover(function(){
		srcimg=$(this).find('img').attr('src');
		var ind=$(this).index();
		$(this).find('img').attr('src','/static/myweb/imgs/active'+ind+'.png');
	},function(){
		$(this).find('img').attr('src',srcimg);
	});
	//end 尾部链接

})