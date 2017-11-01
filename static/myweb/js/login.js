$(function(){
	//判断是否按下自动登录
	var flag1=false;
	$('.login-check').click(function(){
		if(flag1==false){
			$('.login-check div img').css('top','-19px');
			flag1=true;
		}else{
			$('.login-check div img').css('top','0');
			flag1=false;
		}
	});
	//end 判断是否按下自动登录

	//判断输入项是否规范
	var flag = new Array();
	flag['user']=false;
	flag['passwd']=false;
	flag['verify']=false;
	var reg1 = /^1[3,5,8]\d{9}$/;
	var reg2 =/^\w+@\w+[.]\w+$/;
	//判断所有输入项是否规范,规范则可以点击登录按钮
	function panduan(){
		for(i in flag){
			if(!flag[i]){
				return;
			}
		}
		$('.login-btn button').removeAttr('disabled');
	}
	//用户名判断
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
	//密码判断
	$('.login-passwd input').focus(function(){
		$('.form-info').text(' ');
		$('.login-btn button').attr('disabled','disabled');
	});
	$('.login-passwd input').blur(function(){
			var passwdVal=$('.login-passwd input').val();
			if(passwdVal.length>=6){
				flag['passwd']=true;
				panduan()
			}
			else{
				$('.form-info').text('密码格式错误');
				flag['passwd']=false;
				return;
			}
	});
	//验证码判断
	$('input[name=verifycode]').focus(function(){
		$('.form-info').text(' ');
		$('.login-btn button').attr('disabled','disabled');
	});
	$('input[name=verifycode]').blur(function(){
			var code=$('input[name=verifycode]').val();
			if(code.length==4){
				flag['verify']=true;
				panduan()
			}
			else{
				$('.form-info').text('验证码格式错误');
				flag['verify']=false;
			}
	});
	//end 判断输入项是否规范

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