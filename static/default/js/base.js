function checkfan(obj)
{ 
for(i=0;i<document.all(obj).length;i++)
	{
		
	if(document.all(obj)[i].checked)
	{
		document.all(obj)[i].checked=false
	}
else
	{
		document.all(obj)[i].checked=true
	}
	}
	
}

function checkall(obj)
{ 
for(i=0;i<document.all(obj).length;i++)
	{

	document.all(obj)[i].checked=true
	}
	
}

