function mover(element)
{
	element.style.background='rgb(248,252,254)'
	$(element).css('border-left','3px solid rgb(63,138,201)');
	$(element).css('left','-3px');
}
function mout(element)
{
	element.style.background='rgb(255,255,255)'
	$(element).css('border-left','none');
	$(element).css('left','0px');
}