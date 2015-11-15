from django.shortcuts import render_to_response
from models import User,Software,Comment
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
import os, tempfile, zipfile  
from django.core.servers.basehttp import FileWrapper  
# Create your views here.

def first(request):
	#request.session.set_expiry(0)
	if 'log' not in request.session.keys():
		return render_to_response('first.html',{'log':False,'name':''},context_instance=RequestContext(request))
	return render_to_response('first.html',{'log':request.session['log'],'name':request.session['nowuser']},context_instance=RequestContext(request))

def classify(request):
	return render_to_response('classify.html',)

def rank(request):
	return render_to_response('rank.html',)

'''def my(request):
	if 'nowuser' not in request.session.keys():
		return HttpResponse('please login first!')
	name=request.session['nowuser']
	user=User.objects.get(username=name)
	lst=user.softwares.all()
	softs={}
	for soft in lst:
		softname=soft.softname
		print 'softname',softname
		nexturl='/introduction/'+softname+'/'
		imgurl='/static/images/app_images/'+softname+'.png'
		print nexturl,imgurl
		softs[nexturl]=imgurl
	return render_to_response('my.html',{'name':name,'softs':softs})'''

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

def introduction_app(request,app_name):
	url='introduction/'+app_name+'.html'
	return render_to_response(url)

def download_app(request,app_name):
	filename='app/static/softwares/'+app_name+'.apk'
	soft=Software.objects.filter(softname=app_name)[0]
	soft.download_times=soft.download_times+1
	soft.save()
	if 'nowuser' in request.session.keys():
		nowuser=request.session['nowuser']
		user=User.objects.get(username=nowuser)
		user.softwares.add(soft)
	f = open(filename)
	response = HttpResponse(FileWrapper(f), content_type = "application/vnd.android.package-archive")
	response['Content-Encoding']='unicode' 
	response['Content-Length'] = os.path.getsize(filename)
	response['Content-Disposition'] = 'attachment; filename = %s' % f.name
	return response

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
	'''user_input=request.POST['input']
	if user_input:
		soft=Software.objects.filter(called=user_input)
		if soft:
			softname=soft[0].softname
			nexturl='/introduction/'+softname+'/'
			imgurl='/static/images/app_images/'+softname+'.png'
			print 'nexturl',nexturl,imgurl,user_input
			return render_to_response('search_result.html',{'user_input':user_input,'nexturl':nexturl,'imgurl':imgurl})
		else:
			return HttpResponse('search result is null!')
	else:
		return HttpResponseRedirect('/')'''
	return render_to_response('search_result.html')

def oneday(request):
	return render_to_response('topic/2015-11-6.html',locals(),context_instance=RequestContext(request))

def page(request,arg):
	print 'lalalalalalala'
	string='classify/'+arg+'.html'
	return render_to_response(string,context_instance=RequestContext(request))
