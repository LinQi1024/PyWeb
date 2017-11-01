$(function(){
	// 计算总价
	var total=0;
	var pricelist=$('.singeltp');
	
	for(i in pricelist.get()){
		total+=Number($(pricelist.get(i)).text());
	}
	$('.ordertp').find('span').find('span').text(total);
	// end 计算总价

	//城市级联
	$(document).on('change',"select[name=district]",function(){
		//获取选中的id号
		var id = $(this).find("option:selected").attr('pathid');
		$(this).parent('div').nextAll().remove();
		$.ajax({
			url: "/district"+id,
			type: 'get',
			data: {},
			dataType:'json',
			success:function(res){
				if(res.data.length<1)
					return;
				var data = res.data;
				var select = $("<select name=district class=form-control></select>")
				for(var i=0;i<data.length;i++){
					$('<option value="'+data[i].name+'" pathid="'+data[i].id+'">'+data[i].name+'</option>').appendTo(select)
					//$('select:last').append('<option value="'+data[i].id+'">'+data[i].name+'</option>'); 
				}
				var div = $("<div class=col-md-4></div>")
				select.appendTo(div)
				$("select:last").parent('div[class=col-md-4]').after(div);
			}
		});
	});
	//end 城市级联

	//输入框判断正则判断
	var regphone = /^1[3,5,8]\d{9}$/;
	var flag = new Array();
	flag['phone']=true;
	flag['code']=true;
	flag['address']=true;
	//手机号判断
	$('.getgoodinfo input[name=phone]').blur(function() {
		var val=$(this).val();
		if(!regphone.test(val)){
			alert("手机格式错误!");
			flag['phone']=false;
		}
		else{
			flag['phone']=true;
		}
	});
	//详细地址判断
	$('.getgoodinfo input[name=address]').blur(function() {
			var val=$(this).val();
			if(!val){
				alert("详细地址不能为空");
				flag['address']=false;
			}
			else{
				flag['address']=true;
			}
		});
	//邮编判断
	$('.getgoodinfo input[name=code]').blur(function() {
		var val=$(this).val();
		if(val.length!=6){
			alert("邮编格式错误!");
			flag['code']=false;
		}
		else{
			flag['code']=true;
		}
	});
	$('.getgoodinfo form').submit(function() {
		for(i in flag){
			if(flag[i]==false){
				alert('输入信息有误,请重新输入');
				return false;
			}
		}
	});
});