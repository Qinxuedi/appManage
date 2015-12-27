<<<<<<< HEAD
var num=1;
var flag=true;
var active=new Array("null","one","two",'three','four','five');
var sleepy=new Array("null","five","one",'two','three','four');
function validate_required(field,alerttxt)
{
	with (field)
	  {
	  if (value==null||value=="")
	    {alert(alerttxt);return false}
	  else {return true}
	  }
}
function validate_form(thisform)
{
	with (thisform)
	  {
	  if (validate_required(input,"输入不能为空!")==false)
	    {input.focus();return false}
	  }
}
function show_one_picture()
{
	var element=document.getElementById('picture');
	var url="/static/images/first/"+num+".jpg";
	element.src=url;
	document.getElementById(active[num]).src="/static/images/first/active_button.png";
	document.getElementById(sleepy[num]).src="/static/images/first/sleepy_button.png";
	if(flag) num=num+1;
	if(num==6) num=1;
}
function slide()
{
	setInterval('show_one_picture()',1000);
}
function mover(arg)
{
	flag=false;
	var element=document.getElementById(arg);
	element.src="/static/images/first/active_button.png";
	document.getElementById(sleepy[num]).src="/static/images/first/sleepy_button.png";
	switch (arg)
	{
		case 'one':num=1;document.getElementById('picture').src="/static/images/first/1.jpg";break;
		case 'two':num=2;document.getElementById('picture').src="/static/images/first/2.jpg";break;
		case 'three':num=3;document.getElementById('picture').src="/static/images/first/3.jpg";break;
		case 'four':num=4;document.getElementById('picture').src="/static/images/first/4.jpg";break;
		default:num=5;document.getElementById('picture').src="/static/images/first/5.jpg";break;
	}
}
function mout(arg)
{
	flag=true;
	var element=document.getElementById(arg);
	element.src="/static/images/first/sleepy_button.png";
=======
var num=1;
var flag=true;
var active=new Array("null","one","two",'three','four','five');
var sleepy=new Array("null","five","one",'two','three','four');
function validate_required(field,alerttxt)
{
	with (field)
	  {
	  if (value==null||value=="")
	    {alert(alerttxt);return false}
	  else {return true}
	  }
}
function validate_form(thisform)
{
	with (thisform)
	  {
	  if (validate_required(input,"输入不能为空!")==false)
	    {input.focus();return false}
	  }
}
function show_one_picture()
{
	var element=document.getElementById('picture');
	var url="/static/images/first/"+num+".jpg";
	element.src=url;
	document.getElementById(active[num]).src="/static/images/first/active_button.png";
	document.getElementById(sleepy[num]).src="/static/images/first/sleepy_button.png";
	if(flag) num=num+1;
	if(num==6) num=1;
}
function slide()
{
	setInterval('show_one_picture()',1000);
}
function mover(arg)
{
	flag=false;
	var element=document.getElementById(arg);
	element.src="/static/images/first/active_button.png";
	document.getElementById(sleepy[num]).src="/static/images/first/sleepy_button.png";
	switch (arg)
	{
		case 'one':num=1;document.getElementById('picture').src="/static/images/first/1.jpg";break;
		case 'two':num=2;document.getElementById('picture').src="/static/images/first/2.jpg";break;
		case 'three':num=3;document.getElementById('picture').src="/static/images/first/3.jpg";break;
		case 'four':num=4;document.getElementById('picture').src="/static/images/first/4.jpg";break;
		default:num=5;document.getElementById('picture').src="/static/images/first/5.jpg";break;
	}
}
function mout(arg)
{
	flag=true;
	var element=document.getElementById(arg);
	element.src="/static/images/first/sleepy_button.png";
>>>>>>> G
}