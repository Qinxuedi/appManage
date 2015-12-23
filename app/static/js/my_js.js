function mover(element)
{
    element.style.background='rgb(248,252,254)'
}
function mout(element)
{
    element.style.background='rgb(255,255,255)'
}
function collect_mover(element)
{
	element.style.background='rgb(248,252,254)'
	$(element).css('border-left','3px solid rgb(63,138,201)');
	$(element).css('margin-left','-3px');
}
function collect_mout(element)
{
	element.style.background='rgb(255,255,255)'
	$(element).css('border-left','none');
	$(element).css('margin-left','0px');
}
function re_mover(element,arg)
{
	element.style.background='rgb(248,252,254)'
	document.getElementById(arg).style.display='';
}
function re_mout(element,arg)
{
	element.style.background='rgb(255,255,255)'
	document.getElementById(arg).style.display='none';
}
function choose1()
{
	$('#choose1').css('border-bottom', 'solid 2px rgb(250,100,20)');
	$('#choose2').css('border-bottom', 'none');
	document.getElementById('change_div').style.display='none';
	document.getElementById('left_div').style.display='';
	document.getElementById('right_div').style.display='';
}
function choose2()
{
	$('#choose2').css('border-bottom', 'solid 2px rgb(250,100,20)');
	$('#choose1').css('border-bottom', 'none');
	document.getElementById('change_div').style.display='';
	document.getElementById('left_div').style.display='none';
	document.getElementById('right_div').style.display='none';
}