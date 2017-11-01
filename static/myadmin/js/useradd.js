$(function(){
	//城市级联操作
	$.ajax({
		url: "district/0",
		type: 'get',
		data: {},
		dataType:'json',
		success:function(res){
			var data = res.data;
			for(var i=0;i<data.length;i++){
				$('<option value="'+data[i].name+'" pathid="'+data[i].id+'">'+data[i].name+'</option>').appendTo('select:last')
			}
		},
		error:function(){
			alert(url);
			alert("ajax加载失败！");
		}
	});
	//获取最后一个下拉框并添加选中事件
	$("select").live('change',function(){
		//获取选中的id号
		var id = $(this).find("option:selected").attr('pathid');
		$(this).nextAll().remove();
		$.ajax({
			url: "district/"+id,
			type: 'get',
			data: {},
			dataType:'json',
			success:function(res){
				if(res.data.length<1)
					return;
				var data = res.data;
				var select = $("<select name=district></select>")
				for(var i=0;i<data.length;i++){
					$('<option value="'+data[i].name+'" pathid="'+data[i].id+'">'+data[i].name+'</option>').appendTo(select)
					//$('select:last').append('<option value="'+data[i].id+'">'+data[i].name+'</option>'); 
				}
				$("select:last").after(select);
			}
		});
	});

	//标记格式是否都正确
	flag = new Array();
	flag['name'] = false;
	flag['passwd'] = false;
	flag['passwd2'] = false;
	flag['code'] = false;
	flag['phone'] = false;
	flag['email'] = false;

	//手机正则
	var regP = /^1[3,5,8]\d{9}$/;
	//邮箱正则
	var regE = /^\w+@\w+[.]\w+$/;

	//帐号判断
	$('input[name=username]').focus(function(){
		$(this).next('span').html('');
	});
	$('input[name=username]').blur(function(){
		username = $(this).val();
		var res1 = regP.test(username);
		var res2 = regE.test(username);
		if(username==''){
			$(this).next('span').html('帐号不能为空');
			flag['name'] = false;
		}
		else if(!(res1|res2)){
			$(this).next('span').html('帐号格式错误');
			flag['name'] = false;
		}
		else{
			flag['name'] = true;
		}
	})

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
	})

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