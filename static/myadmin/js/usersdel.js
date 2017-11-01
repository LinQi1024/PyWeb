$(function(){
	//删除提示
	$('.btn-del').click(function(){
		var val = confirm('删除后数据不可恢复!')
		if(!val){
			return false;
		}
	});
})