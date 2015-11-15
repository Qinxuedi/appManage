function chooseDiv(element,arg)
{
    $('.show_div').css('display','none');
    document.getElementById(arg).style.display='';
    $('.choose').css('border-top','solid 1px rgb(230,230,230)');
    $(element).css('border-top','solid 3px rgb(92,184,92)');
}
function mover(element,arg)
{
	element.style.background='rgb(248,252,254)'
	document.getElementById(arg).style.display='';
}
function mout(element,arg)
{
	element.style.background='rgb(255,255,255)'
	document.getElementById(arg).style.display='none';
}