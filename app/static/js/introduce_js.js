<<<<<<< HEAD
var now_page=1
var app_id;
var page_num;
var now_platform;
function validate_form2(element)
{
    var keyword=document.getElementById('comment_text').value
    if(keyword=="") 
    {
        alert("输入不能为空!")
        return false;
    }
    return true;
}
function init()
{
    now_platform=3;
	app_id=document.getElementById('app_id').value
	page_num=parseInt(document.getElementById('page_id').value)
	var html=new Array();
    for(i=1;i<=page_num;i++)
    {
    	html[i]='<a href="#up_up" class="one_page" onclick="return click_page(this)">'+i+'</a>'
    }
    html[1]='<a href="#up_up" class="one_page" onclick="return click_page(this)" style="background: rgb(122,199,32);">'+now_page+'</a>'
    for(i=2;i<=page_num;i++)
    {
    	html[i]=html[i-1]+html[i]
    }
    document.getElementById('real_page').innerHTML=html[page_num]
}
function click_page(element)
{
    $('.one_page').css('background','white');
    element.style.background='rgb(122,199,32);'
    var page_id=element.innerHTML
    now_page=parseInt(page_id)
    $.ajax({
        method:'GET',
        url:'/get_page',
        cache:false,
        dataType:'json',
        data:{'page_id':page_id,'now_platform':now_platform,},
        success:function(result)
        {
            document.getElementById('real_comment').innerHTML=result
        },
        error:function(result)
        {
            alert('error!')
        }
    })
}
function click_platform(element)
{
    var platform_id=element.value;
    now_platform=parseInt(element.value);
    now_page=1;
    $.ajax({
        method:'GET',
        url:'/get_platform_init',
        cache:false,
        dataType:'json',
        data:{'platform_id':platform_id,},
        success:function(result)
        {
            document.getElementById('forjson').innerHTML=result
        },
        error:function(result)
        {
            alert('error!')
        }
    })
}
function chooseDiv(element,arg)
{
    $('.classify').css('display','none');
    document.getElementById(arg).style.display='';
    $('.choose').css('border-top','solid 1px rgb(230,230,230)');
    $(element).css('border-top','solid 3px rgb(92,184,92)');
    /*$.ajax({
        method:'GET',
        url:'/get_app',
        cache:false,
        dataType:'json',
        //data:{'page_id':page_id,'comment_id':app_id,},
        success:function(result)
        {
            document.getElementById('iphone').innerHTML=result
        },
        error:function(result)
        {
            alert('error!')
        }
    })*/
}
function mover(element,arg)
{
	element.style.background='rgb(248,252,254)'
}
function mout(element,arg)
{
	element.style.background='rgb(255,255,255)'
}
=======
var now_page=1
var app_id;
var page_num;
function init()
{
	app_id=document.getElementById('app_id').value
	page_num=parseInt(document.getElementById('page_id').value)
	var html=new Array();
    for(i=1;i<=page_num;i++)
    {
    	html[i]='<a href="#up_up" class="one_page" onclick="return click_page(this)">'+i+'</a>'
    }
    html[1]='<a href="#up_up" class="one_page" onclick="return click_page(this)" style="background: rgb(122,199,32);">'+now_page+'</a>'
    for(i=2;i<=page_num;i++)
    {
    	html[i]=html[i-1]+html[i]
    }
    document.getElementById('real_page').innerHTML=html[page_num]
}
function click_page(element)
{
    $('.one_page').css('background','white');
    element.style.background='rgb(122,199,32);'
    var page_id=element.innerHTML
    now_page=parseInt(page_id)
    if(now_page!=1)
    {
        document.getElementById('up_page').style.display='inline-block'
    }
    else
    {
        document.getElementById('up_page').style.display='none'
    }
    if(now_page!=page_num)
    {
        document.getElementById('down_page').style.display='inline-block'
    }
    else
    {
        document.getElementById('down_page').style.display='none'
    }
    $.ajax({
        method:'GET',
        url:'/get_page',
        cache:false,
        dataType:'json',
        data:{'page_id':page_id,'comment_id':app_id,},
        success:function(result)
        {
            document.getElementById('real_comment').innerHTML=result
        },
        error:function(result)
        {
            alert('error!')
        }
    })
}
function up_page()
{
    var page_id=now_page-1+''
    now_page=parseInt(page_id)
    if(now_page!=1)
    {
        document.getElementById('up_page').style.display='inline-block'
    }
    else
    {
        document.getElementById('up_page').style.display='none'
    }
    if(now_page!=page_num)
    {
        document.getElementById('down_page').style.display='inline-block'
    }
    else
    {
        document.getElementById('down_page').style.display='none'
    }
    var html=new Array();
    for(i=1;i<=page_num;i++)
    {
    	html[i]='<a href="#up_up" class="one_page" onclick="return click_page(this)">'+i+'</a>'
    }
    html[now_page]='<a href="#up_up" class="one_page" onclick="return click_page(this)" style="background: rgb(122,199,32);">'+now_page+'</a>'
    for(i=2;i<=page_num;i++)
    {
    	html[i]=html[i-1]+html[i]
    }
    document.getElementById('real_page').innerHTML=html[page_num]
    $.ajax({
        method:'GET',
        url:'/get_page',
        cache:false,
        dataType:'json',
        data:{'page_id':page_id,'comment_id':app_id,},
        success:function(result)
        {
            document.getElementById('real_comment').innerHTML=result
        },
        error:function(result)
        {
            alert('error!')
        }
    })
}
function down_page()
{
    var page_id=now_page+1+''
    now_page=parseInt(page_id)
    if(now_page!=1)
    {
        document.getElementById('up_page').style.display='inline-block'
    }
    else
    {
        document.getElementById('up_page').style.display='none'
    }
    if(now_page!=page_num)
    {
        document.getElementById('down_page').style.display='inline-block'
    }
    else
    {
        document.getElementById('down_page').style.display='none'
    }
    var html=new Array();
    for(i=1;i<=page_num;i++)
    {
    	html[i]='<a href="#up_up" class="one_page" onclick="return click_page(this)">'+i+'</a>'
    }
    html[now_page]='<a href="#up_up" class="one_page" onclick="return click_page(this)" style="background: rgb(122,199,32);">'+now_page+'</a>'
    for(i=2;i<=page_num;i++)
    {
    	html[i]=html[i-1]+html[i]
    }
    document.getElementById('real_page').innerHTML=html[page_num]
    $.ajax({
        method:'GET',
        url:'/get_page',
        cache:false,
        dataType:'json',
        data:{'page_id':page_id,'comment_id':app_id,},
        success:function(result)
        {
            document.getElementById('real_comment').innerHTML=result
        },
        error:function(result)
        {
            alert('error!')
        }
    })
}
function chooseDiv(element,arg)
{
    $('.classify').css('display','none');
    document.getElementById(arg).style.display='';
    $('.choose').css('border-top','solid 1px rgb(230,230,230)');
    $(element).css('border-top','solid 3px rgb(92,184,92)');
    /*$.ajax({
        method:'GET',
        url:'/get_app',
        cache:false,
        dataType:'json',
        //data:{'page_id':page_id,'comment_id':app_id,},
        success:function(result)
        {
            document.getElementById('iphone').innerHTML=result
        },
        error:function(result)
        {
            alert('error!')
        }
    })*/
}
function mover(element,arg)
{
	element.style.background='rgb(248,252,254)'
}
function mout(element,arg)
{
	element.style.background='rgb(255,255,255)'
}
>>>>>>> G
