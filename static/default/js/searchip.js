$("#mymodel").click(function(){
	 var ip = $("#ip").val();
   	 $.post("../compute/getdetail/",{'ip':ip}, function(ret){
   		    $('#identifier').modal('show');
            $('#result').html(ret);      
       })
       	
})


$("#chart").click(function(){
	 var ip = $("#result").text();
   	 $.post("../compute/getchart/",{'ip':ip}, function(ret){
             $('#result').html(ret)   
        })
})

$("#open").click(function(){
	 var ip = $("#result").text();
   	 $.post("../compute/openip/",{'ip':ip}, function(ret){
             $('#result').html(ret)   
        })
})

$("#shutdown").click(function(){
	 var ip = $("#result").text();
   	 $.post("../compute/shutdown/",{'ip':ip}, function(ret){
             $('#result').html(ret)   
        })
})

$("#close").click(function(){
	location.reload()   
})

 $(".btn-lg").click(function(){
	 var ip = $(this).button().text()
	 $.post("../compute/getdetail/",{'ip':ip}, function(ret){  
		     $('#identifier').modal('show') 
             $('#result').html(ret) 
        })
 })

