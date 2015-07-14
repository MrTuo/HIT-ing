from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import *
from django.contrib import auth
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
	if req.session.get('username',''):
		return HttpResponseRedirect('/topic/index')
	if req.POST:
		post=req.POST
		logname=post["name"]
		logpassword=post["password"]

		if User.objects.filter(username=logname):
			user = auth.authenticate(username = logname, password = logpassword)
			if user is not None:
				if user.is_active:
					auth.login(req,user)
					req.session['username']=logname
					return HttpResponseRedirect('/topic/index')
				else:
					er_message="not active"
			else:
				er_message="psword error"

		else :
			er_message="not exist!"
	return render_to_response('login.html',{'er_message':er_message})				

def logout(req):
	auth.logout(req)
	return HttpResponseRedirect('/topic/index')

def index(req):
	user=''
	if req.session.get('username',''):
		username=req.session['username']
		try:
			user=User.objects.get(username=username)
		except:
			pass
	return render_to_response('index.html',{'user':user})