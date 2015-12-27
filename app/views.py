#coding=utf-8
from django.shortcuts import render_to_response
from models import recommend_app,rank_app
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
import os, tempfile, zipfile  
from django.core.servers.basehttp import FileWrapper
import re,json
import requests
import urllib2,os
# Create your views here.
catch=False
all_comments=[]
all_comments_android=[]
all_comments_iphone=[]
all_comments_ipad=[]
now_platform=3

def first(request):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}
    
    if catch==True:
        apps=recommend_app.objects.filter(position=1).delete()
        html_2_5_search = 'http://app.91.com'
        html_2_5_search =requests.get(html_2_5_search,headers=headers).text
        pic=["1"]*100
        name=["1"]*100
        pic[0] =re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fl">(.*?)<img(.*?)data-original="(.*?)"',html_2_5_search,re.S).group(4)
        name[0] =re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fl">(.*?)<img(.*?)alt="(.*?)"',html_2_5_search,re.S).group(4)
        pic[1] =re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fl">(.*?)<li(.*?)<li(.*?)data-original="(.*?)"',html_2_5_search,re.S).group(5)
        name[1] =re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fl">(.*?)<li(.*?)<li(.*?)alt="(.*?)"',html_2_5_search,re.S).group(5)
        pic[2]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fl">(.*?)<li(.*?)<li(.*?)<li(.*?)data-original="(.*?)"',html_2_5_search,re.S).group(6)
        name[2]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fl">(.*?)<li(.*?)<li(.*?)<li(.*?)alt="(.*?)"',html_2_5_search,re.S).group(6)
        pic[3]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fl">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)data-original="(.*?)"',html_2_5_search,re.S).group(7)
        name[3]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fl">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)alt="(.*?)"',html_2_5_search,re.S).group(7)
        pic[4]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fl">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)data-original="(.*?)"',html_2_5_search,re.S).group(8)
        name[4]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fl">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)alt="(.*?)"',html_2_5_search,re.S).group(8)
        pic[5]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fr">(.*?)<img(.*?)data-original="(.*?)"',html_2_5_search,re.S).group(4)
        name[5]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fr">(.*?)<img(.*?)alt="(.*?)"',html_2_5_search,re.S).group(4)
        pic[6] =re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fr">(.*?)<li(.*?)<li(.*?)data-original="(.*?)"',html_2_5_search,re.S).group(5)
        name[6] =re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fr">(.*?)<li(.*?)<li(.*?)alt="(.*?)"',html_2_5_search,re.S).group(5)
        pic[7]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fr">(.*?)<li(.*?)<li(.*?)<li(.*?)data-original="(.*?)"',html_2_5_search,re.S).group(6)
        name[7]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fr">(.*?)<li(.*?)<li(.*?)<li(.*?)alt="(.*?)"',html_2_5_search,re.S).group(6)
        pic[8]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fr">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)data-original="(.*?)"',html_2_5_search,re.S).group(7)
        name[8]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fr">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)alt="(.*?)"',html_2_5_search,re.S).group(7)
        pic[9]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fr">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)data-original="(.*?)"',html_2_5_search,re.S).group(8)
        name[9]=re.search('<div class="mt10 clearfix" id="ib_soft">(.*?)<div class="cate_box l_box fr">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)alt="(.*?)"',html_2_5_search,re.S).group(8)
        #v1=[]

        for i in range(0,10):
            #print pic[i]
            picture=requests.get(pic[i],headers=headers)
            pic_url='app/static/images/first/hot/'+str(i)+'.png'
            fp=open(pic_url,'wb')
            fp.write(picture.content)
            fp.close
            if len(name[i])>=7:
                tmp=name[i][0:5]+'...'
            else:
                tmp=name[i]
            #v1.append((pic_url,tmp,"/introduction/?app_name="+name[i],name[i]))
            #print "/introduction/?app_name="+name[i]
            #print len("/introduction/?app_name="+name[i])
            app=recommend_app(pic_url='/static/images/first/hot/'+str(i)+'.png',show=tmp,url="/introduction/?app_name="+name[i],name=name[i],position=1)
            app.save()
    v1=recommend_app.objects.filter(position=1)
    hot_first=v1[0]
    v1=v1[1:]

    if catch==True:
        apps=recommend_app.objects.filter(position=2).delete()
        html_2_6_search = 'http://apk.hiapk.com/apps/Tools?sort=5&pi=1'
        html_2_6_search =requests.get(html_2_6_search,headers=headers).text
        pic_1=["1"]*100
        name_1=["1"]*100
        pic_1[0]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)src="(.*?)"',html_2_6_search,re.S).group(3)
        name_1[0]=re.search('<ul id="appSoftListBox">(.*?)<span(.*?)<a(.*?)>(.*?)</a>',html_2_6_search,re.S).group(4)
        pic_1[1]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_6_search,re.S).group(4)
        name_1[1]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<span(.*?)<a(.*?)>(.*?)</a>',html_2_6_search,re.S).group(6)
        pic_1[2]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_6_search,re.S).group(5)
        name_1[2]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<span(.*?)<a(.*?)>(.*?)</a>',html_2_6_search,re.S).group(7)
        pic_1[3]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_6_search,re.S).group(6)
        name_1[3]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<span(.*?)<a(.*?)>(.*?)</a>',html_2_6_search,re.S).group(8)
        pic_1[4]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_6_search,re.S).group(7)
        name_1[4]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<span(.*?)<a(.*?)>(.*?)</a>',html_2_6_search,re.S).group(9)
        pic_1[5]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_6_search,re.S).group(8)
        name_1[5]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<span(.*?)<a(.*?)>(.*?)</a>',html_2_6_search,re.S).group(10)
        pic_1[6]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_6_search,re.S).group(9)
        name_1[6]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<span(.*?)<a(.*?)>(.*?)</a>',html_2_6_search,re.S).group(11)
        pic_1[7]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_6_search,re.S).group(10)
        name_1[7]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<span(.*?)<a(.*?)>(.*?)</a>',html_2_6_search,re.S).group(12)
        pic_1[8]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_6_search,re.S).group(11)
        name_1[8]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<span(.*?)<a(.*?)>(.*?)</a>',html_2_6_search,re.S).group(13)
        pic_1[9]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_6_search,re.S).group(12)
        name_1[9]=re.search('<ul id="appSoftListBox">(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<span(.*?)<a(.*?)>(.*?)</a>',html_2_6_search,re.S).group(14)
        for i in range(0,10):
            #print pic_1[i]
            picture=requests.get(pic_1[i],headers=headers)
            pic_url='app/static/images/first/new/'+str(i)+'.png'
            fp=open(pic_url,'wb')
            fp.write(picture.content)
            fp.close
            if len(name_1[i])>=7:
                tmp=name_1[i][0:5]+'...'
            else:
                tmp=name_1[i]
            app=recommend_app(pic_url='/static/images/first/new/'+str(i)+'.png',show=tmp,url="/introduction/?app_name="+name_1[i],name=name_1[i],position=2)
            app.save()
    v2=recommend_app.objects.filter(position=2)
    new_first=v2[0]
    v2=v2[1:]
    
    if catch==True:
        apps=recommend_app.objects.filter(position=3).delete()
        try:
            url_1_1_search = 'http://app.91.com/soft/'
            html_1_1_search = requests.get(url_1_1_search,headers=headers).text
            html_1_1_search = re.findall('<div class="topic_before">(.*?)data-original="(.*?)"(.*?)alt="(.*?)"',html_1_1_search,re.S)
            for i in range(2,12):
                print 'name=',html_1_1_search[i][3]
                if len(html_1_1_search[i][3])>=7:
                    name=html_1_1_search[i][3][0:5]+'...'
                else:
                    name=html_1_1_search[i][3]

                picture=requests.get(html_1_1_search[i][1],headers=headers)
                pic_url='app/static/images/first/fivestar/'+str(i-2)+'.png'
                fp=open(pic_url,'wb')
                fp.write(picture.content)
                fp.close
                app=recommend_app(pic_url='/static/images/first/fivestar/'+str(i-2)+'.png',show=name,url="/introduction/?app_name="+html_1_1_search[i][3],name=html_1_1_search[i][3],position=3)
                app.save()
                #v3.append((html_1_1_search[i][1],name,"/introduction/?app_name="+html_1_1_search[i][3],html_1_1_search[i][3]))
        except Exception,ex:
            pass
    v3=recommend_app.objects.filter(position=3)
    fivestar_first=v3[0]
    v3=v3[1:]

    if catch==True:
        apps=recommend_app.objects.filter(position=4).delete()
        html_2_7_search = 'http://sj.zol.com.cn/android_bibei'
        html_2_7_search =requests.get(html_2_7_search,headers=headers).text
        pic_2=["1"]*100
        name_2=["1"]*100
        pic_2[0]=re.search('<ul class="android_list clearfix"(.*?)<li(.*?)src="(.*?)"',html_2_7_search,re.S).group(3)
        name_2[0]=re.search('<ul class="android_list clearfix"(.*?)<li(.*?)title="(.*?)"',html_2_7_search,re.S).group(3)
        pic_2[1]=re.search('<ul class="android_list clearfix"(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_7_search,re.S).group(4)
        name_2[1]=re.search('<ul class="android_list clearfix"(.*?)<li(.*?)<li(.*?)title="(.*?)"',html_2_7_search,re.S).group(4)
        pic_2[2]=re.search('<ul class="android_list clearfix"(.*?)<li(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_7_search,re.S).group(5)
        name_2[2]=re.search('<ul class="android_list clearfix"(.*?)<li(.*?)<li(.*?)<li(.*?)title="(.*?)"',html_2_7_search,re.S).group(5)
        pic_2[3]=re.search('<ul class="android_list clearfix"(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_7_search,re.S).group(6)
        name_2[3]=re.search('<ul class="android_list clearfix"(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)title="(.*?)"',html_2_7_search,re.S).group(6)
        pic_2[4]=re.search('<ul class="android_list clearfix"(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_7_search,re.S).group(7)
        name_2[4]=re.search('<ul class="android_list clearfix"(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)<li(.*?)title="(.*?)"',html_2_7_search,re.S).group(7)
        pic_2[5] =re.search('<div class="section">(.*?)class="section"(.*?)class="section"(.*?)<li(.*?)src="(.*?)"',html_2_7_search,re.S).group(5)
        name_2[5] =re.search('<div class="section">(.*?)class="section"(.*?)class="section"(.*?)<li(.*?)title="(.*?)"',html_2_7_search,re.S).group(5)
        pic_2[6] =re.search('<div class="section">(.*?)class="section"(.*?)class="section"(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_7_search,re.S).group(6)
        name_2[6] =re.search('<div class="section">(.*?)class="section"(.*?)class="section"(.*?)<li(.*?)<li(.*?)title="(.*?)"',html_2_7_search,re.S).group(6)
        pic_2[7] =re.search('<div class="section">(.*?)class="section"(.*?)class="section"(.*?)class="section"(.*?)<li(.*?)src="(.*?)"',html_2_7_search,re.S).group(6)
        name_2[7] =re.search('<div class="section">(.*?)class="section"(.*?)class="section"(.*?)class="section"(.*?)<li(.*?)title="(.*?)"',html_2_7_search,re.S).group(6)
        pic_2[8] =re.search('<div class="section">(.*?)class="section"(.*?)class="section"(.*?)class="section"(.*?)<li(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_7_search,re.S).group(8)
        name_2[8] =re.search('<div class="section">(.*?)class="section"(.*?)class="section"(.*?)class="section"(.*?)<li(.*?)<li(.*?)<li(.*?)title="(.*?)"',html_2_7_search,re.S).group(8)
        pic_2[9] =re.search('<div class="section">(.*?)class="section"(.*?)class="section"(.*?)class="section"(.*?)<li(.*?)<li(.*?)src="(.*?)"',html_2_7_search,re.S).group(7)
        name_2[9] =re.search('<div class="section">(.*?)class="section"(.*?)class="section"(.*?)class="section"(.*?)<li(.*?)<li(.*?)title="(.*?)"',html_2_7_search,re.S).group(7)
        for i in range(0,10):
            picture=requests.get(pic_2[i],headers=headers)
            pic_url='app/static/images/first/must/'+str(i)+'.png'
            fp=open(pic_url,'wb')
            fp.write(picture.content)
            fp.close
            if len(name_2[i])>=7:
                tmp=name_2[i][0:5]+'...'
            else:
                tmp=name_2[i]
            app=recommend_app(pic_url='/static/images/first/must/'+str(i)+'.png',show=tmp,url="/introduction/?app_name="+name_2[i],name=name_2[i],position=4)
            app.save()
            #v4.append((pic_2[i],tmp,"/introduction/?app_name="+name_2[i],name_2[i]))
    v4=recommend_app.objects.filter(position=4)
    must_first=v4[0]
    v4=v4[1:]

    if catch==True:
        apps=recommend_app.objects.filter(position=5).delete()
        try:
            url_1_2_search = 'http://app.91.com/sort/0_1_12_1'
            html_1_2_search = requests.get(url_1_2_search,headers=headers).text
            html_1_2_search = re.findall('<div class="topic_before">(.*?)data-original="(.*?)"(.*?)alt="(.*?)"',html_1_2_search,re.S)
            for i in range(2,12):
                if len(html_1_2_search[i][3])>=7:
                    name=html_1_2_search[i][3][0:5]+'...'
                else:
                    name=html_1_2_search[i][3]
                #v5.append((html_1_2_search[i][1],name,"/introduction/?app_name="+html_1_2_search[i][3],html_1_2_search[i][3]))
                picture=requests.get(html_1_2_search[i][1],headers=headers)
                pic_url='app/static/images/first/game/'+str(i-2)+'.png'
                fp=open(pic_url,'wb')
                fp.write(picture.content)
                fp.close
                app=recommend_app(pic_url='/static/images/first/game/'+str(i-2)+'.png',show=name,url="/introduction/?app_name="+html_1_2_search[i][3],name=html_1_2_search[i][3],position=5)
                app.save()
        except Exception,ex:
            pass
    v5=recommend_app.objects.filter(position=5)
    game_first=v5[0]
    v5=v5[1:]

    return render_to_response('first.html',locals(),context_instance=RequestContext(request))

def classify(request,arg1,arg2):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}
    id1=int(arg1)
    id2=int(arg2)
    red=[]
    for i in range(1,23):
        red.append(False)
    if id1>=1453 and id1<=1465:
        red[id1-1453]=True
    elif id1>=1466 and id1<=1472:
        red[id1-1452]=True
    elif id1==1491:
        red[13]=True
    elif id1==1892:
        red[21]=True
    if id2==1:
        url='http://dl.pconline.com.cn/sort/'+arg1+'-1.html'
    else:
        url='http://dl.pconline.com.cn/sort/'+arg1+'-1'+'-'+arg2+'.html'
    html=requests.get(url,headers=headers).text
    number=int((re.search('<strong>(.*?)<em>(.*?)</em></strong>',html,re.S).group(2))[1:-1])
    if number%10==0:
        number=number/10
    else:
        number=number/10+1
    #共11个，若id2<=8,显示1~9；若id2>=number-7,显示number-8~number
    show=[]  #(id=true,now=true,value,href)
    if number<=11:
        for i in range(1,number+1):
            show.append((True,False,i,'/classify/'+str(id1)+'/'+str(i)))
        show[id2-1]=(True,True,id2,'/classify/'+str(id1)+'/'+str(id2))
    elif id2<=8:
        for i in range(1,10):
            show.append((True,False,i,'/classify/'+str(id1)+'/'+str(i)))
        show[id2-1]=(True,True,id2,'/classify/'+str(id1)+'/'+str(id2))
        show.append((False,False,'...'))
        show.append((True,False,number,'/classify/'+str(id1)+'/'+str(number)))
    elif id2>=number-7:
        show.append((True,False,1,'/classify/'+str(id1)+'/1'))
        show.append((False,False,'...'))
        for i in range(number-8,number+1):
            show.append((True,False,i,'/classify/'+str(id1)+'/'+str(i)))
        show[id2-number-1]=(True,True,id2,'/classify/'+str(id1)+'/'+str(id2))
    else:
        show.append((True,False,1,'/classify/'+str(id1)+'/1'))
        show.append((False,False,"..."))
        for i in range(id2-3,id2+4):
            show.append((True,False,i,'/classify/'+str(id1)+'/'+str(i)))
        show[5]=(True,True,id2,'/classify/'+str(id1)+'/'+str(id2))
        show.append((False,False,'...'))
        show.append((True,False,number,'/classify/'+str(id1)+'/'+str(number)))
    up=True
    down=True
    up_href='/classify/'+str(id1)+'/'+str(id2-1)
    down_href='/classify/'+str(id1)+'/'+str(id2+1)
    if id2==1:up=False
    if id2==number:down=False
    lst1=re.findall('<div class="listPic"><img alt="(.*?)" src="(.*?)"></div>',html,re.S)
    lst2=re.findall('<div class="lcDes">(.*?)<span>(.*?)</span>(.*?)<p>(.*?)<a',html,re.S)
    lst=[]
    filename='app/static/images/classify/'+str(id1)+'/'+str(id2)+'/'+'0.jpg'
    if os.path.exists(filename):
        exists=True
    else:
        exists=False
        os.makedirs('app/static/images/classify/'+str(id1)+'/'+str(id2)+'/')
    for i in range(0,len(lst1)):
        name=[]
        for j in range(0,len(lst1[i][0])):
            if lst1[i][0][j]!=' ' and lst1[i][0][j]!=' ':
                name.append(lst1[i][0][j])
            else:
                break
        if id1==1454 and id2==1 and (i==2 or i==3):
            continue
        if id1==1454 and id2==1 and i==1:
            name=name[2:4]
        if exists==False:
            pic=requests.get(lst1[i][1],headers=headers)
            fp=open('app/static/images/classify/'+str(id1)+'/'+str(id2)+'/'+str(i)+'.jpg','wb')
            fp.write(pic.content)
            fp.close
        url='/introduction/?app_name='+''.join(name)
        lst.append((''.join(name),'/static/images/classify/'+str(id1)+'/'+str(id2)+'/'+str(i)+'.jpg',lst2[i][3],url))
    return render_to_response('classify.html',locals(),context_instance=RequestContext(request))

def rank(request,arg):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}
    id=int(arg)
    show=[]
    for i in range(1,8):
        show.append((i,False,'/rank/'+str(i)+'/'))
    show[id-1]=(id,True,'/rank/'+str(id)+'/')
    up=True
    down=True
    if id==1:up=False
    if id==7:down=False
    up_href='/rank/'+str(id-1)+'/'
    down_href='/rank/'+str(id+1)+'/'

    if catch==True:
        rank_app.objects.all().delete()
        for page in range(1,8):
            url='http://as.baidu.com/a/rank?cid=100&s=1&f=web_alad%40next&pn='+str(page)
            html=urllib2.urlopen(url).read().decode('utf-8')
            v=re.findall('<div class="normal-wrap">(.*?)<img src="(.*?)" alt="(.*?)">(.*?)<div class="s-index-star s-index-star-(.*?)">(.*?)<span class="s-index-icon down-icon">&nbsp;</span>(.*?)</div>',html,re.S)
            #lst=[]
            for i in range(0,len(v)):
                star=int(v[i][4])
                pic=requests.get(v[i][1],headers=headers)
                fp=open('app/static/images/rank/'+str(page)+'/'+str(i)+'.jpg','wb')
                fp.write(pic.content)
                fp.close
                url='/introduction/?app_name='+v[i][2]
                print 'name=',v[i][2]
                application=rank_app(pic_url='/static/images/rank/'+str(page)+'/'+str(i)+'.jpg',name=v[i][2],star=star,download=v[i][6],rank=(page-1)*40+i+1,url=url)
                application.save()
            #lst.append(('/static/images/rank/'+arg+'/'+str(i)+'.jpg',v[i][2],tmp,v[i][6],(id-1)*40+i+1,url)) 
            #img,name,star,download,rank,introduction_url
    v=rank_app.objects.order_by('rank')[(id-1)*40:id*40]
    lst=[]
    for i in range(0,40):
        star=v[i].star
        if star%2==1:
                star=star/2+1
        else:
            star=star/2
        tmp=[]
        for j in range(1,star+1):
            tmp.append("/static/images/app_images/yellowstar.png")
        for j in range(star+1,6):
            tmp.append("/static/images/app_images/greystar.png")
        lst.append((v[i].pic_url,v[i].name,tmp,v[i].download,v[i].rank,v[i].url))
    print lst
    return render_to_response('rank.html',locals(),context_instance=RequestContext(request))


def my(request):
    return render_to_response('my.html')

def today(request):
    return render_to_response('today.html',)

def login(request):
    if 'name' in request.POST and request.POST['name']:
        name=request.POST['name']
        mima=request.POST['mima']
        user=User.objects.filter(username=name)
        if user:
            if user[0].password==mima:
                request.session['log']=True
                request.session['nowuser']=name
                return HttpResponseRedirect('/')
            else:
                return render_to_response('login.html',{'exit':True,'correct':False},context_instance=RequestContext(request))
        else:
            return render_to_response('login.html',{'exit':False,'correct':True},context_instance=RequestContext(request))
    return render_to_response('login.html',{'exit':True,'correct':True},context_instance=RequestContext(request))

def register(request):
    if 'name' in request.POST and request.POST['name']:
        name=request.POST['name']
        mima1=request.POST['mima1']
        mima2=request.POST['mima2']
        user=User.objects.filter(username=name)
        if user:
            return render_to_response('register.html',{'exit':True,'same':True,'success':False},context_instance=RequestContext(request))
        else:
            if mima1==mima2:
                user=User(username=name,password=mima1)
                user.save()
                return render_to_response('register.html',{'exit':False,'same':True,'success':True},context_instance=RequestContext(request))
            else:
                return render_to_response('register.html',{'exit':False,'same':False,'success':False},context_instance=RequestContext(request))
    return render_to_response('register.html',{'exit':False,'same':True,'success':False},context_instance=RequestContext(request))

def logout(request):
    del request.session['log']
    del request.session['nowuser']
    return HttpResponseRedirect('/')

def introduction_app(request):
    global all_comments_android,all_comments_iphone,all_comments_ipad,all_comments
    all_comments=[]
    all_comments_android=[]
    all_comments_iphone=[]
    all_comments_ipad=[]
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}
    app_name = request.GET['app_name'].encode('utf8')

    v1=[]#for iphone

    #http://app.91.com 91游戏中心
    try:
        star=[]
        html_1_1_search = 'http://app.91.com/soft/iphone/search/1_5_0_0_'+app_name
        html_1_1_search =requests.get(html_1_1_search).text
        url_1_1_real = 'http://app.91.com'+re.search('<div class="zoom">(.*?)<a href="(.*?)"',html_1_1_search,re.S).group(2)
        html_1_1_real = requests.get(url_1_1_real).text
        html_1_1_version = re.search('<ul class="s_info">(.*?)<li>(.*?)<a',html_1_1_real,re.S).group(2)
        bool = 0
        for char in html_1_1_version:
            if char=='a':
                bool=1
                break
        if bool:
            html_1_1_version = re.search('(.*?)<a',html_1_1_version,re.S).group(1)
        html_1_1_version =  html_1_1_version.strip()[3:]
        html_1_1_big = re.search('<ul class="s_info">(.*?)<li>(.*?)<li>(.*?)<li>(.*?)</li>',html_1_1_real,re.S).group(4)
        html_1_1_big = html_1_1_big.strip()[5:]
        html_1_1_star = re.search('<span class="spr star">(.*?)</a></span>',html_1_1_real,re.S).group(1)
        html_1_1_star = int(re.findall('(\d+)',html_1_1_star,re.S)[0][0])
        for i in range(1,html_1_1_star+1):
            star.append("/static/images/app_images/yellowstar.png")
        for i in range(html_1_1_star+1,6):
            star.append("/static/images/app_images/greystar.png")
        v1.append((html_1_1_version,html_1_1_big,star,url_1_1_real,'91应用中心'))
    except Exception,ex:
            pass
    #http://www.xyzs.com XY手机助手
    try:
        star=[]
        url_1_2_search='http://www.xyzs.com/search/?keyword='+app_name
        html_1_2_search=requests.get(url_1_2_search,headers=headers).text
        url_1_2_real='http://www.xyzs.com'+re.search('<h4 class="talkbox">(.*?)<a href="(.*?)"',html_1_2_search,re.S).group(2)
        html_1_2_real=requests.get(url_1_2_real,headers=headers).text
        html_1_2_star=re.search('<strong class="pngimg" style="width:(.*?)%;"></strong>',html_1_2_real,re.S).group(1)
        html_1_2_star=int(html_1_2_star)/20
        html_1_2_real=re.search('<h1 id="title">(.*?)</h1>(.*?)</p>(.*?)<p>(.*?)</p>(.*?)<p>(.*?)</p>(.*?)<p>(.*?)</p>',html_1_2_real,re.S)
        html_1_2_version=html_1_2_real.group(6).strip()[3:]
        html_1_2_big=html_1_2_real.group(8).strip()[3:]
        for i in range(1,html_1_2_star+1):
            star.append("/static/images/app_images/yellowstar.png")
        for i in range(html_1_2_star+1,6):
            star.append("/static/images/app_images/greystar.png")
        v1.append((html_1_2_version,html_1_2_big,star,url_1_2_real,'XY苹果助手'))
    except Exception,ex:
        pass
    #http://www.app111.com 苹果园
    try:
        star=[]
        url_1_3_search='http://www.app111.com/search?k='+app_name
        html_1_3_search=requests.get(url_1_3_search,headers=headers).text
        url_1_3_real='http://www.app111.com'+re.search('<div class="APPer_contain3_1">(.*?)<a title=(.*?)href="(.*?)"',html_1_3_search,re.S).group(3)
        html_1_3_real=requests.get(url_1_3_real,headers=headers).text
        html_1_3_star = re.search('<div class="num">(.*?)<span>(.*?)</span>',html_1_3_real,re.S).group(2)
        html_1_3_star = int(re.findall('(\d+)',html_1_3_star,re.S)[0][0])/2
        html_1_3_big=re.search('<div class="app_summary"(.*?)<p>(.*?)</p>',html_1_3_real,re.S)
        html_1_3_big=html_1_3_big.group(2).strip()[5:]
        html_1_3_version=re.search('<div id="divdetails"(.*?)</div>',html_1_3_real,re.S)
        html_1_3_version=re.findall('(\d+)',html_1_3_version.group(1),re.S)
        html_1_3_version=html_1_3_version[4][0]+'.'+html_1_3_version[5][0]+'.'+html_1_3_version[6][0]
        for i in range(1,html_1_3_star+1):
            star.append("/static/images/app_images/yellowstar.png")
        for i in range(html_1_3_star+1,6):
            star.append("/static/images/app_images/greystar.png")
        v1.append((html_1_3_version,html_1_3_big,star,url_1_3_real,'苹果园'))
    except Exception,ex:
        pass
    #http://ios.25pp.com pp助手
    try:
        star=[]
        url_1_4_search='http://ios.25pp.com/search/2_0_0_0_1/'+app_name
        html_1_4_search=requests.get(url_1_4_search,headers=headers).text
        url_1_4_real=re.search('<a class="h4_a" href="(.*?)"',html_1_4_search,re.S).group(1)
        html_1_4_real=requests.get(url_1_4_real,headers=headers).text
        html_1_4_big=re.search('<div class="txt">(.*?)<li>(.*?)</li>(.*?)<li>(.*?)</li>(.*?)<li>(.*?)</li>',html_1_4_real,re.S).group(6)
        html_1_4_big=html_1_4_big.strip()[9:]
        html_1_4_version=re.search('<div class="txt">(.*?)<li>(.*?)</li>(.*?)<li>(.*?)</li>(.*?)<li>(.*?)</li>',html_1_4_real,re.S).group(2)
        html_1_4_version=html_1_4_version.strip()[9:]
        html_1_4_star=re.search('<li class="borderR">(.*?)<li>(.*?)<span>(.*?)</span>',html_1_4_real,re.S).group(3)
        html_1_4_star = int(re.findall('(\d+)',html_1_4_star,re.S)[0][0])
        for i in range(1,html_1_4_star+1):
            star.append("/static/images/app_images/yellowstar.png")
        for i in range(html_1_4_star+1,6):
            star.append("/static/images/app_images/greystar.png")
        v1.append((html_1_4_version,html_1_4_big,star,url_1_4_real,'pp助手'))
    except Exception,ex:
        pass

    v2=[]#for ipad

    #http://app.91.com 91游戏中心
    try:
        star=[]
        html_2_1_search = 'http://app.91.com/soft/iphone/search/1_5_0_0_'+app_name
        html_2_1_search =requests.get(html_2_1_search).text
        url_2_1_real = 'http://app.91.com'+re.search('<div class="zoom">(.*?)<a href="(.*?)"',html_2_1_search,re.S).group(2)
        html_2_1_real = requests.get(url_2_1_real).text
        html_2_1_version = re.search('<ul class="s_info">(.*?)<li>(.*?)</li>',html_2_1_real,re.S).group(2)
        bool = 0
        for char in html_2_1_version:
            if char=='a':
                bool=1
                break
        if bool:
            html_2_1_version = re.search('(.*?)<a',html_2_1_version,re.S).group(1)
        html_2_1_version =  html_2_1_version.strip()[3:]
        html_2_1_big = re.search('<ul class="s_info">(.*?)<li>(.*?)<li>(.*?)<li>(.*?)</li>',html_2_1_real,re.S).group(4)
        html_2_1_big = html_2_1_big.strip()[5:]
        html_2_1_star = re.search('<span class="spr star">(.*?)</a></span>',html_2_1_real,re.S).group(1)
        html_2_1_star = int(re.findall('(\d+)',html_2_1_star,re.S)[0][0])
        for i in range(1,html_2_1_star+1):
            star.append("/static/images/app_images/yellowstar.png")
        for i in range(html_2_1_star+1,6):
            star.append("/static/images/app_images/greystar.png")
        v2.append((html_2_1_version,html_2_1_big,star,url_2_1_real,'91应用中心'))
    except Exception,ex:
        pass
    #http://www.xyzs.com XY手机助手
    try:
        star=[]
        html_2_3_search = 'http://www.xyzs.com/search/index/ipad_all_1/?keyword='+app_name
        html_2_3_search =requests.get(html_2_3_search).text
        url_2_3_real = 'http://www.xyzs.com'+re.search('<div class="seventyfiveL">(.*?)<a href="(.*?)"',html_2_3_search,re.S).group(2)
        html_2_3_real = requests.get(url_2_3_real).text
        html_2_3_version = re.search('<div class="SpecialGameRecommend">(.*?)<p>(.*?)</p>(.*?)<p>(.*?)</p>(.*?)<p>(.*?)</p>',html_2_3_real,re.S).group(6)
        html_2_3_big = re.search('<div class="SpecialGameRecommend">(.*?)<p>(.*?)</p>(.*?)<p>(.*?)</p>(.*?)<p>(.*?)</p>(.*?)<p>(.*?)</p>',html_2_3_real,re.S).group(8)
        html_2_3_star = re.search('<div class="GameAppDetailGrade pngimg">(.*?)<strong class="pngimg" style="(.*?)"',html_2_3_real,re.S).group(2)
        html_2_3_star = int(re.findall('(\d+)',html_2_3_star,re.S)[0][0])
        html_2_3_star = html_2_3_star/2
        for i in range(1,html_2_3_star+1):
            star.append("/static/images/app_images/yellowstar.png")
        for i in range(html_2_3_star+1,6):
            star.append("/static/images/app_images/greystar.png")
        v2.append((html_2_3_version[3:],html_2_3_big[3:],star,url_2_3_real,'XY苹果助手'))
    except Exception,ex:
        pass
    #http://www.app111.com/ 苹果园  
    try:
        star=[]
        html_2_4_search = 'http://www.app111.com/search?k='+app_name
        html_2_4_search =requests.get(html_2_4_search).text
        url_2_4_real = 'http://www.app111.com'+re.search('<div class="APPer_contain3_1">(.*?)<a title="(.*?)" style="(.*?)" href="(.*?)"',html_2_4_search,re.S).group(4)
        html_2_4_real = requests.get(url_2_4_real).text
        html_2_4_version = re.search('<div class="app_summary">(.*?)<div id=(.*?)>(.*?)<p>(.*?)</p>(.*?)<p>(.*?)</p>(.*?)<p>(.*?)</p>(.*?)<p>(.*?)</p>',html_2_4_real,re.S).group(10)
        html_2_4_version = html_2_4_version.strip()
        html_2_4_big = re.search('<div class="app_summary" id="divdetailsout">(.*?)<p>(.*?)</p>',html_2_4_real,re.S).group(2)
        html_2_4_big = html_2_4_big.strip()
        html_2_4_star = re.search('<div class="num">(.*?)<span>(.*?)</span>',html_2_4_real,re.S).group(2)
        html_2_4_star = int(re.findall('(\d+)',html_2_4_star,re.S)[0][0])
        html_2_4_star = int(html_2_4_star/2)
        for i in range(1,html_2_4_star+1):
            star.append("/static/images/app_images/yellowstar.png")
        for i in range(html_2_4_star+1,6):
            star.append("/static/images/app_images/greystar.png")
        v2.append((html_2_4_version[5:],html_2_4_big[5:],star,url_2_4_real,'苹果园'))
    except Exception,ex:
        pass
    #http://www.25pp.com/ PP助手
    try:
        star=[]
        html_2_2_search = 'http://www.25pp.com/search/?devtype=all&a=soft&keyword='+app_name
        html_2_2_search =requests.get(html_2_2_search).text
        url_2_2_real = 'http://www.25pp.com'+re.search('<div id="contentArea" class="app_list">(.*?)<a href="(.*?)"',html_2_2_search,re.S).group(2)
        html_2_2_real = requests.get(url_2_2_real).text
        html_2_2_version = re.search('<ul class="edition">(.*?)<li>(.*?)<span>(.*?)</span>',html_2_2_real,re.S).group(3)
        html_2_2_big = re.search('<ul class="edition">(.*?)<li>(.*?)</li>(.*?)<li>(.*?)</li>(.*?)<li>(.*?)<span>(.*?)</span>',html_2_2_real,re.S).group(7)
        html_2_2_star = re.search('<div class="star2">(.*?)<div class="gradeStar1">(.*?)</div>(.*?)<h3>(.*?)<span>(.*?)</span>',html_2_2_real,re.S).group(5)
        html_2_2_star = int(re.findall('(\d+)',html_2_2_star,re.S)[0][0])
        for i in range(1,html_2_2_star+1):
            star.append("/static/images/app_images/yellowstar.png")
        for i in range(html_2_2_star+1,6):
            star.append("/static/images/app_images/greystar.png")
        v2.append((html_2_2_version,html_2_2_big,star,url_2_2_real,'PP助手'))
    except Exception,ex:
        pass

    v3=[]
    try:
        #http://apk.hiapk.com 安卓市场
        star=[]
        #print 'app_name:',app_name
        url_3_1_search='http://apk.hiapk.com/search?key='+app_name+'&pid=0'
        html_3_1_search=requests.get(url_3_1_search,headers=headers).text
        url_3_1_real='http://apk.hiapk.com'+re.search('<span class="list_title font12"><a href="(.*?)">(.*?)</a></span>',html_3_1_search,re.S).group(1)
        html_3_1_real=requests.get(url_3_1_real,headers=headers).text
        html_3_1_version=re.search('<div id="appSoftName" class="detail_title left">(.*?)\((.*?)\)(.*?)</div>',html_3_1_real,re.S).group(2)
        html_3_1_big=re.search('<span id="appSize" class="font14">(.*?)MB</span>',html_3_1_real,re.S).group(1)+'MB'
        html_3_1_star=int(re.search('<div class="star_bg  star_m_(.)(.) left"></div>',html_3_1_real,re.S).group(1))
        for i in range(1,html_3_1_star+1):
            star.append("/static/images/app_images/yellowstar.png")
        for i in range(html_3_1_star+1,6):
            star.append("/static/images/app_images/greystar.png")
        v3.append((html_3_1_version,html_3_1_big,star,url_3_1_real,'安卓市场'))
    except Exception,ex:
        pass

    try:
        #https://www.wandoujia.com 豌豆荚
        url_3_2_search='http://www.wandoujia.com/search?key='+app_name+'&source=apps'
        html_3_2_search=requests.get(url_3_2_search,headers=headers).text
        url_3_2_real=re.search('<div class="icon-wrap">(.*?)<a href="(.*?)" target="_blank">',html_3_2_search,re.S).group(2)
        print url_3_2_real
        html_3_2_real=requests.get(url_3_2_real,headers=headers).text
        img3=re.search('<div class="app-icon">(.*?)<img src="(.*?)"(.*?)" />(.*?)</div>',html_3_2_real,re.S).group(2)
        html_3_2_version=re.search('id="baidu_time" itemprop="datePublished" datetime="(.*?)">(.*?)</time></dd>(.*?)<dt>(.*?)</dt>(.*?)<dd>(.*?)</dd>',html_3_2_real,re.S).group(6)
        html_3_2_big=re.search('<dd>(.*?)M(.*?)<meta itemprop="fileSize" content="(.*?)"/>(.*?)</dd>',html_3_2_real,re.S).group(1)
        html_3_2_big_big=[]
        for char in html_3_2_big:
            if (char>='0' and char<='9') or char=='.':
                html_3_2_big_big.append(char)
        if star:
            v3.append((html_3_2_version,''.join(html_3_2_big_big)+'MB',star,url_3_2_real,'豌豆荚'))
    except Exception,ex:
        pass

    try:
        #http://zhushou.360.cn 360手机助手「微信」
        star=[]
        url_3_3_search='http://zhushou.360.cn/search/index/?kw='+app_name
        html_3_3_search=requests.get(url_3_3_search,headers=headers).text
        url_3_3_real='http://zhushou.360.cn'+re.search('<dt><a href="(.*?)">',html_3_3_search,re.S).group(1)
        html_3_3_real=requests.get(url_3_3_real,headers=headers).text
        img3=re.search('<dt><img src="(.*?)" width="72" height="72" alt="(.*?)"></dt>',html_3_3_real,re.S).group(1)
        title3=re.search('<p><strong>(.*?)</strong>(.*?)</p>',html_3_3_real,re.S).group(2)
        html_3_3_version=re.search('<td><strong>(.*?)</strong>(.*?)<!--(.*?)--><!--(.*?)--></td>',html_3_3_real,re.S).group(2)
        html_3_3_big=re.search('<span class="s-3">(.*?)</span>(.*?)<span class="s-3">(.*?)M</span>',html_3_3_real,re.S).group(3)
        html_3_3_star=float(re.search('<div class="(.*?)" id="votePanel">(.*?)<h2>(.*?)<span>(.*?)</span>',html_3_3_real,re.S).group(4))/2
        html_3_3_star=int(round(html_3_3_star))
        for i in range(1,html_3_3_star+1):
            star.append("/static/images/app_images/yellowstar.png")
        for i in range(html_3_3_star+1,6):
            star.append("/static/images/app_images/greystar.png")
        v3.append((html_3_3_version,html_3_3_big+'MB',star,url_3_3_real,'360手机助手'))
    except Exception,ex:
        pass

    '''try:
        url_3_4_search='http://apk.91.com/soft/android/search/1_5_0_0_'+app_name
        html_3_4_search=requests.get(url_3_4_search,headers=headers).text
        html_3_4_this=re.search('<div class="zoom">(.*?)</div>',html_3_4_search,re.S).group(1)
        url_3_4_real='http://apk.91.com'+re.search('<h4><a href="(.*?)">',html_3_4_this,re.S).group(1)
        html_real=requests.get(url_3_4_real,headers=headers).text
        html_3_4_history=re.search('<ul class="version_list">(.*?)</ul>',html_real,re.S).group(1)
        #print html_3_4_history
        tmp=re.findall('<a href="(.*?)">(.*?)</a>',html_3_4_history,re.S)
        for i in range(0,len(tmp)):
            one=[]
            three=[]
            zero='http://apk.91.com'+tmp[i][0]
            for char in tmp[i][1]:
                if char>='0' and char<='9' or char=='.':
                    one.append(char)
            html_soft=requests.get(zero,headers=headers).text
            #print html_soft
            html_need=re.search('<ul class="s_info">(.*?)</ul>',html_soft,re.S).group(0)
            html_star=int(re.search('<a class="w(.) spr">',html_soft,re.S).group(1))
            star=[]
            for j in range(1,html_star+1):
                star.append("/static/images/app_images/yellowstar.png")
            for j in range(html_star+1,6):
                star.append("/static/images/app_images/greystar.png")
            html_big=re.search('<li>[\u4e00-\u9fa5]*(.*?)MB</li>',html_need,re.S).group(1)
            for j in range(len(html_big)-1,0,-1):
                if html_big[j]>='0' and html_big[j]<='9' or html_big[j]=='.':
                    three.append(html_big[j])
                else:
                    break
            #print html_star
            #html_big=html_group.group(3)
            tmp[i]=(''.join(one),''.join(list(reversed(three)))+'MB',star,zero,'91助手')
        v3=v3+tmp
    except Exception,ex:
        pass'''
    v3.sort(cmp=t)

    comment_search_url='http://shouji.baidu.com/s?wd='+app_name+'&data_type=app&f=header_app%40input%40btn_search&from=landing'
    comment_html=requests.get(comment_search_url,headers=headers).text
    comment_app_url='http://shouji.baidu.com'+re.search('<div class="top">(.*?)<a(.*?)href="(.*?)"',comment_html,re.S).group(3)
    comment_real_html=requests.get(comment_app_url,headers=headers).text
    comment_id=re.search('<input type="hidden" name="groupid" value="(.*?)" />',comment_real_html,re.S).group(1)
    comment_url="http://shouji.baidu.com/comment?action_type=getCommentList&groupid="+comment_id+"&pn=10"
    comment_value=requests.get(comment_url,headers=headers).text
    tmp=re.findall('<p>(.*?)</p>(.*?)<div class="comment-time">(.*?) (.*?)</div>',comment_value,re.S)
    comment_page=0
    if tmp:
        comment_page=10
    else:
        for i in range (9,0,-1):
            comment_url="http://shouji.baidu.com/comment?action_type=getCommentList&groupid="+comment_id+"&pn="+str(i)
            comment_value=requests.get(comment_url,headers=headers).text
            tmp=re.findall('<p>(.*?)</p>(.*?)<div class="comment-time">(.*?) (.*?)</div>',comment_value,re.S)
            if tmp:
                comment_page=i
                break
    down=True
    search_comment_url='/search_comment/'
    if comment_page<=1:
        down=False
    show=[]
    for i in range(0,comment_page):
        show.append(i+1)

    comments=[]
    if comment_page!=0:
        comment_url="http://shouji.baidu.com/comment?action_type=getCommentList&groupid="+comment_id+"&pn=1"
        comment_value=requests.get(comment_url,headers=headers).text
        tmp=re.findall('<p>(.*?)</p>(.*?)<div class="comment-time">(.*?) (.*?)</div>',comment_value,re.S)
    for item in tmp:
        comments.append((item[0],item[2]))

    for i in range(1,comment_page+1):
        comment_url="http://shouji.baidu.com/comment?action_type=getCommentList&groupid="+comment_id+"&pn="+str(i)
        comment_value=requests.get(comment_url,headers=headers).text
        tmp=re.findall('<p>(.*?)</p>(.*?)<div class="comment-time">(.*?) (.*?)</div>',comment_value,re.S)
        for item in tmp:
            all_comments.append((item[0],item[2]))
            if len(item[0])%3==2:
                all_comments_android.append((item[0],item[2]))
            elif len(item[0])%3==1:
                all_comments_iphone.append((item[0],item[2]))
            else:
                all_comments_ipad.append((item[0],item[2]))

    app_name = request.GET['app_name'].encode('utf8')
    recommend=True
    try:
        rec=[]
        url_1_5_search='http://apk.hiapk.com/search?key='+app_name+'&pid=0'
        html_1_5_search=requests.get(url_1_5_search,headers=headers).text
        url_1_5_real='http://apk.hiapk.com'+re.search('<span class="list_title font12">(.*?)<a href="(.*?)">',html_1_5_search,re.S).group(2)
        html_1_5_real=requests.get(url_1_5_real,headers=headers).text
        html_1_5_real=re.findall('<dl class="soft_item_dl">(.*?)src="(.*?)"(.*?)alt="(.*?)"',html_1_5_real,re.S)
        for i in range(0,5):
            #print html_1_5_real[i][1]
            #print html_1_5_real[i][3]
            rec.append((html_1_5_real[i][1],html_1_5_real[i][3],"/introduction/?app_name="+html_1_5_real[i][3]))
    except Exception,ex:
        recommend=False
        pass

    return render_to_response('introduce.html',locals(),context_instance=RequestContext(request))

def t(x,y):
    version1=x[0]
    version2=y[0]
    lst1=version1.split('.')
    lst2=version2.split('.')
    for i in range(0,len(lst1)):
        try:
            lst1[i]=int(lst1[i])
        except Exception,ex:
            lst1[i]=0
    for i in range(0,len(lst2)):
        try:
            lst2[i]=int(lst2[i])
        except Exception,ex:
            lst2[i]=0
    return -cmp(lst1,lst2)

def get_page(request):
    global all_comments_android,all_comments_iphone,all_comments_ipad,all_comments
    result={}
    page_id=request.GET['page_id']
    now_platform=int(request.GET['now_platform'])
    comments=[]

    print now_platform

    if now_platform==3:
        beginIndex=(int(page_id)-1)*10
        endIndex=min(int(page_id)*10,len(all_comments)-1)
        for item in all_comments[beginIndex:endIndex]:
            comments.append("<div class='one_comment'><div class='comment_inf'><p class='main_comment'>"+item[0]+"</p></div><div class='c_date'><label>"+u'\u53d1\u5e03\u65e5\u671f'+":</label><label>"+item[1]+"</label></div><br></div>")
    elif now_platform==2:
        beginIndex=(int(page_id)-1)*10
        endIndex=min(int(page_id)*10,len(all_comments_android)-1)
        for item in all_comments_android[beginIndex:endIndex]:
            comments.append("<div class='one_comment'><div class='comment_inf'><p class='main_comment'>"+item[0]+"</p></div><div class='c_date'><label>"+u'\u53d1\u5e03\u65e5\u671f'+":</label><label>"+item[1]+"</label></div><br></div>")
    elif now_platform==1:
        beginIndex=(int(page_id)-1)*10
        endIndex=min(int(page_id)*10,len(all_comments_iphone)-1)
        for item in all_comments_iphone[beginIndex:endIndex]:
            comments.append("<div class='one_comment'><div class='comment_inf'><p class='main_comment'>"+item[0]+"</p></div><div class='c_date'><label>"+u'\u53d1\u5e03\u65e5\u671f'+":</label><label>"+item[1]+"</label></div><br></div>")
    else:
        beginIndex=(int(page_id)-1)*10
        endIndex=min(int(page_id)*10,len(all_comments_ipad)-1)
        for item in all_comments_ipad[beginIndex:endIndex]:
            comments.append("<div class='one_comment'><div class='comment_inf'><p class='main_comment'>"+item[0]+"</p></div><div class='c_date'><label>"+u'\u53d1\u5e03\u65e5\u671f'+":</label><label>"+item[1]+"</label></div><br></div>")

    length=len(comments)
    for i in range(1,length):
        comments[i]=comments[i-1]+comments[i]

    result=comments[length-1]
    result=json.dumps(result)
    #print 'result',result
    return HttpResponse(result,content_type='application/json')

def get_platform_init(request):
    global now_platform
    print 'I am in get_platform'
    result={}
    platform_id=request.GET['platform_id']
    now_platform=int(platform_id)
    comments=[]
    comments.append("<div id='real_comment'>")
    pages=0
    if platform_id=='3':
        pages=len(all_comments)
        print 'pages=len(all_comments)',pages
        for item in all_comments[0:10]:
            comments.append("<div class='one_comment'><div class='comment_inf'><p class='main_comment'>"+item[0]+"</p></div><div class='c_date'><label>"+u'\u53d1\u5e03\u65e5\u671f'+":</label><label>"+item[1]+"</label></div><br></div>")
    elif platform_id=='2':
        pages=len(all_comments_android)
        for item in all_comments_android[0:10]:
            comments.append("<div class='one_comment'><div class='comment_inf'><p class='main_comment'>"+item[0]+"</p></div><div class='c_date'><label>"+u'\u53d1\u5e03\u65e5\u671f'+":</label><label>"+item[1]+"</label></div><br></div>")
    elif platform_id=='1':
        pages=len(all_comments_iphone)
        for item in all_comments_iphone[0:10]:
            comments.append("<div class='one_comment'><div class='comment_inf'><p class='main_comment'>"+item[0]+"</p></div><div class='c_date'><label>"+u'\u53d1\u5e03\u65e5\u671f'+":</label><label>"+item[1]+"</label></div><br></div>")
    else:
        pages=len(all_comments_ipad)
        for item in all_comments_ipad[0:10]:
            comments.append("<div class='one_comment'><div class='comment_inf'><p class='main_comment'>"+item[0]+"</p></div><div class='c_date'><label>"+u'\u53d1\u5e03\u65e5\u671f'+":</label><label>"+item[1]+"</label></div><br></div>")
    if pages%10==0:
        pages=pages/10
    else:
        pages=pages/10+1
    comments.append("</div><div class='blank' id='blank1'></div><div id='page'><div id='real_page'>")

    if pages>0:
        comments.append("<a href='#up_up' class='one_page' onclick='return click_page(this)' style='background: rgb(122,199,32);'>1</a>")
    
    for i in range(2,pages+1):
        comments.append("<a href='#up_up' class='one_page' onclick='return click_page(this)'>"+str(i)+"</a>")
    length=len(comments)
    for i in range(1,length):
        comments[i]=comments[i-1]+comments[i]

    result=comments[length-1]
    result=json.dumps(result)
    #print 'result',result
    return HttpResponse(result,content_type='application/json')

def search_comment(request):
    global now_platform
    keyword=request.POST['keyword']

    comments=[]
    if now_platform==3:
        for item in all_comments:
            if keyword in item[0]:
                comments.append((item[0],item[1]))
    elif now_platform==2:
        for item in all_comments_android:
            if keyword in item[0]:
                comments.append((item[0],item[1]))
    elif now_platform==1:
        for item in all_comments_iphone:
            if keyword in item[0]:
                comments.append((item[0],item[1]))
    else:
        for item in all_comments_ipad:
            if keyword in item[0]:
                comments.append((item[0],item[1]))
    return render_to_response('search_comment.html',locals(),context_instance=RequestContext(request))


def change_password(request):
    if 'nowmima' in request.POST and request.POST['nowmima']:
        nowmima=request.POST['nowmima']
        mima1=request.POST['mima1']
        mima2=request.POST['mima2']
        name=request.session['nowuser']
        user=User.objects.get(username=name)
        realmima=user.password
        if nowmima!=realmima:
            return render_to_response('change_password.html',{'correct':False,'same':True,'success':False},context_instance=RequestContext(request))
        else:
            if mima1==mima2:
                user.password=mima1
                user.save()
                #do something th change password
                return render_to_response('change_password.html',{'correct':True,'same':True,'success':True},context_instance=RequestContext(request))
            else:
                return render_to_response('change_password.html',{'correct':True,'same':False,'success':False},context_instance=RequestContext(request))
    return render_to_response('change_password.html',{'correct':True,'same':True,'success':False},context_instance=RequestContext(request))

def search_result(request):
    app_name=request.POST['input']
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}
    #安卓市场
    try:
        lst1=[]
        url_1_search='http://apk.hiapk.com/search?key='+app_name+'&pid=0'
        html_1_search=requests.get(url_1_search,headers=headers).text
        tmp1=re.findall('<span class="list_title font12"><a href="(.*?)">(.*?)</a></span>',html_1_search,re.S)
        tmp2=re.findall('<div class="list_description">(.*?) </div> ',html_1_search,re.S)
        tmp3=re.findall('<img width="72px" height="72px" src="(.*?)" />',html_1_search,re.S)
        if len(tmp1)>15:
            tmp1=tmp1[0:15]
            tmp2=tmp2[0:15]
            tmp3=tmp3[0:15]
        for i in range(0,len(tmp1)):
            tmp_str=[]
            j=0
            k=0
            while k<len(tmp2[i]):
                if tmp2[i][k:k+5]=='<br/>':
                    k=k+5
                    continue
                if tmp2[i][k:k+6]=='<br />':
                    k=k+6
                    continue
                if tmp2[i][k]!=' ' and tmp2[i][k]!='\n':
                    tmp_str.append(tmp2[i][k])
                    j+=1
                if j>=102:
                    tmp_str.append('...')
                    break
                k+=1
            url='/introduction/?app_name='+tmp1[i][1]
            lst1.append((tmp1[i][1],''.join(tmp_str),tmp3[i],url))
    except Exception,ex:
        pass

    try:
        lst2=[]
        url_2_search='http://www.wandoujia.com/search?key='+app_name+'&source=apps'
        html_2_search=requests.get(url_2_search,headers=headers).text
        tmp1=re.findall('<a href="(.*?)" target="_blank" title="(.*?)" class="name">',html_2_search,re.S)
        tmp2=re.findall('<div class="comment">(.*?)</div>',html_2_search,re.S)
        tmp3=re.findall('<img src="(.*?)" width="68" height="68"',html_2_search,re.S)
        if len(tmp1)>15:
            tmp1=tmp1[0:15]
            tmp2=tmp2[0:15]
            tmp3=tmp3[0:15]
        for i in range(0,len(tmp1)):
            tmp_str=[]
            j=0
            k=0
            while k<len(tmp2[i]):
                if tmp2[i][k:k+5]=='<br/>':
                    k+=5
                    continue
                if tmp2[i][k:k+6]=='<br />':
                    k+=6
                    continue
                if tmp2[i][k]!=' ' and tmp2[i][k]!='\n':
                    tmp_str.append(tmp2[i][k])
                    j+=1
                if j>=102:
                    tmp_str.append('...')
                    break
                k+=1
            url='/introduction/?app_name='+tmp1[i][1]
            lst2.append((tmp1[i][1],''.join(tmp_str),tmp3[i],url))
    except Exception,ex:
        pass

    '''lst3=[]
    url_3_search='http://app.91.com/soft/iphone/search/1_5_0_0_'+app_name
    html_3_search=requests.get(url_3_search,headers=headers).text
    tmp=re.findall('<img class="lazy" src="(.*?)" data-original="(.*?)"(.*?)<div class="zoom">(.*?)<h4><a href="(.*?)">(.*?)</a></h4>(.*?)<p>(.*?)</p>',html_3_search,re.S)
    if len(tmp)>10:
        tmp=tmp[0:10]
    print tmp
    for i in range(0,len(tmp)):
        url='/introduction/?app_name='+tmp[i][1]
        lst3.append((tmp[i][6],tmp[i][7],tmp[i][1],url))
    print 'lst3',lst3'''
    length1=len(lst1)
    length2=len(lst2)
    length=length2
    if length1>length:length=length1
    lst=[]
    for i in range(0,length):
        if i<length2:
            flag=True
            for item in lst:
                if item[0]==lst2[i][0]:
                    flag=False
            if flag:
                lst.append(lst2[i])
        if i<length1:
            flag=True
            for item in lst:
                if item[0]==lst1[i][0]:
                    flag=False
            if flag:
                lst.append(lst1[i])
    number=len(lst)
    return render_to_response('search_result.html',locals(),context_instance=RequestContext(request))

def oneday(request):
    return render_to_response('topic/2015-11-6.html',locals(),context_instance=RequestContext(request))

def page(request,arg):
    string='classify/'+arg+'.html'
    return render_to_response(string,context_instance=RequestContext(request))
