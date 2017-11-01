$(function(){
	$('.goodsdel').click(function(){	
		var flag = confirm("确定删除?");
		if(!flag){
			return false;
		}	
	})
});