$(function(){
	//城市级联
	$("select[name=district]").live('change',function(){
		//获取选中的id号
		var id = $(this).find("option:selected").attr('pathid');
		$(this).nextAll().remove();
		$.ajax({
			url: "/district"+id,
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
	//详细地址不能为空
	var flag = true;
	$('input[name=address]').focus(function(){
		$(this).next('span').html('')
	});
	$('input[name=address]').blur(function(){
		code = $(this).val();
		if(code.length== ''){
			$(this).next('span').html('详细地址不能为空');
			flag = false;
		}
		else{
			flag = true;
		}
	});
	//提交前确认格式是否都正确
	$('form').submit(function() {
		if(flag==false){
			alert('详细地址不能为空');
			return false;
		}
	});
})