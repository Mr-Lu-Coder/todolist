function change(obj)
{
	var ids = ''
	for(i=0;i<obj.length;i++)
	{
		 var id = obj[i].value
		 ids+=id+':'
	}
	return ids
}

function update(checkbox,ip,mac,pcname,username){
	    
		var ids = ''
		var temps = ''
		var flog = 0
		for(i=0;i<document.all(checkbox).length;i++)
		{
			var id = document.all(checkbox)[i].nextSibling.nodeValue
			ids+=id+':'
			if(document.all(checkbox)[i].checked)
				{
					temp = '1'
					flog = 1
				}
			else
				{
					temp = '0'
				}
			temps+=temp+':'
		}
		if (flog != 1)
		{
			alert("没选择修改的行")
			document.location.reload()
			return 
		}
		checkbox = temps
		mac = change(document.all(mac))
		pcname = change(document.all(pcname))
		ip = change(document.all(ip))
		$.post("../compute/updatecompute",{'ids':ids,'ip':ip,'checkbox':checkbox,'pcname':pcname,'mac':mac}, function(ret){
			if (ret == '1')
				{
					alert("修改成功")
					document.location.reload() 
				}
			else 
				{
					alert("修改失败，请联系管理员")
					document.location.reload()
				}
		})
}

function del(obj)
{ 
	var ids = ''
for(i=0;i<document.all(obj).length;i++)
	{
	if(document.all(obj)[i].checked)
		{
			 var id = document.all(obj)[i].nextSibling.nodeValue
		  	 ids+=id+':'
		  	 document.all(obj)[i].checked = false
		}
	}
	
	$.post("../compute/delcompute",{'ids':ids}, function(ret){
    location.reload()   
	})	
}