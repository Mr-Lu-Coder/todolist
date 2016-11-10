$("#addall").click(function(){
	 var ip = $("#target").val();
	 var h1= document.getElementsByTagName("h1")[0];
	 h1.innerHTML = "等待时间过长，内部处理，成功后会提醒";
   	 $.post("../compute/alladd/",{'ip':ip}, function(ret){
   		 	alert("自动配置成功") ;
        })
})