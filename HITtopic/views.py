from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import *
from django.contrib.auth.models import User

# Create your views here.
def register(req):
	er_message=''
	if req.POST:
		post=req.POST
		new_name=post['name']
		new_email=post['email']
		new_password=post['password']
		if User.objects.filter(username=new_name):
			er_message='exist'
		elif new_password!=post['re_password']:
			er_message='not match'
		else:
			new_User=User.objects.create_user(username=new_name,password=new_password)
			new_MyUser=MyUser(user=new_User,email=new_email,permission=1)
			new_MyUser.save()
			new_User.save()
			return HttpResponseRedirect('/topic/login')

	return render_to_response('register.html',{'er_message':er_message}) 

def login(req):
	er_message=""
	if req.session.get('name',''):
		#return HttpResponseRedirect('/topic/index')
		return HttpResponse('hello')
	if req.POST:
		post=req.POST
		logname=post["name"]
		logpassword=post["password"]
		if User.objects.filter(username="logname"):
			user = auth.authenticate(username = logname, password = logpassword)
			if user is not None:
				if user.is_active:
					auth.login(req,user)
				else:
					er_message="not active"
			else:
				er_message="psword error"
		else :
			er_message="not exist!"
	return render_to_response('login.html',{'er_message':er_message})				



def index(req):
	if req.session.get('name',''):
		username=req.session['name']
		user=MyUser.objects.filter(name=username)
	else:
		username=''
	if req.POST:
		del req.session['name']
		return HttpResponseRedirect('/topic/register')	
	return render_to_response('index.html',{'user':username})