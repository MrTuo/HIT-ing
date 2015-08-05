#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from models import *
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
##################################################
#                     用户登录、注册和登出



def register(req):
	er_message=''#返回非法输入的错误信息

	postname=""
	postemail=""#记录传入信息以避免用户重复输入

	if req.POST:
		post=req.POST
		new_name=post['name']
		new_email=post['email']
		new_password=post['password']

		postname=new_name
		postemail=new_email

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

	return render_to_response('register.html',{'er_message':er_message,\
												 'postname':postname,\
												'postemail':postemail}) 

def login(req):
	er_message=""

	postname=""#记录传入信息以避免用户重复输入

	if req.session.get('username',''):
		return HttpResponseRedirect('/topic/index')
	if req.POST:
		post=req.POST
		logname=post["name"]
		logpassword=post["password"]
		postname=logname
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
	return render_to_response('login.html',{'er_message':er_message,\
											'postname':postname})				

def logout(req):
	auth.logout(req)
	return HttpResponseRedirect('/topic/index')
######################################################################

def index(req):
	'''
	主页面显示
	'''
	user=''
	if req.session.get('username',''):
		username=req.session['username']
		try:
			user=User.objects.get(username=username)
		except:
			pass
	query=''
	if req.GET:
		query=req.GET.get('q','')
		if query:
			topic_list=Topic.objects.filter(title__icontains=query)
		else:
			topic_list=Topic.objects.order_by('-pub_date')
	else:
		topic_list=Topic.objects.order_by('-pub_date')

	return render_to_response('index.html',{'user':user,\
											'topic_list':topic_list,\
											'query':query})


def create_topic(req):
	'''
	发表新的话题
	'''
	user=''
	username=req.session.get('username','')
	if username:
		user= User.objects.get(username=username)
	if req.POST:
		post=req.POST
		new_title=post['title']
		new_content=post['content']
		new_topic=Topic(title=new_title, content=new_content, author=user )
		new_topic.save()
		print "success"
		return HttpResponseRedirect('/topic/index')
	return render_to_response('create_topic.html',{'user':user})

def detail(req,offset):
	'''
	话题详情以及评论
	'''
	user=''
	username=req.session.get('username','')
	if username:
		user= User.objects.get(username=username)
	topic=Topic.objects.get(id=offset)
	comment_list=Comment.objects.filter(topic=topic)
	if req.POST:
		post=req.POST
		comment_content=post['content']
		new_comment=Comment(user=user,topic=topic,content=comment_content)
		new_comment.save()
		topic.comment_num+=1;
		topic.save()
	return render_to_response('detail.html',{'topic':topic,'user':user,'comment_list':comment_list})



