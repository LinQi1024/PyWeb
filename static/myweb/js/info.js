 $(function(){
    var flag=$('h2:eq(0)').attr('flag')
    function jump(count) { 
        window.setTimeout(function(){ 
            count--; 
            if(count > 0) { 
                $('seconds').text(count); 
                jump(count); 
            } else { 
                //判断类型,跳转到不同页面
                if (flag == 'cartadd') {
                    history.go(-2); 
                }
                else{
                    location.href = '/login'
                }
                
            } 
        }, 1000); 
    } 
    jump(1); 
 });
