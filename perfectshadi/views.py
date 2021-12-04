from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Contact
from admin01.models import story
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
	stry=[]
	sobj=story.objects.all()
	for i in sobj:
		stry.append(i)
	return render(request,'index.html',{'stry':stry})


def form2(request):    
	if request.method=="POST":
		fname=request.POST['fname']
		lname=request.POST['lname']
		uname=request.POST['uname']
		email=request.POST['email']
		mobile=request.POST['mobile']
		dob=request.POST['dob']
		utype=request.POST['utype']
		pwd=request.POST['pwd']

		try:
			userobj=User(first_name=fname,last_name=lname,username=uname,password=make_password(pwd),email=email)
			userobj.save()

			user_profile=UserProfile(user=userobj,dob=dob,usertype=utype,mobile=mobile)
			user_profile.save()
			messages.success(request,"Account registered Successfully!")
			return redirect('/index/')
		except:
			messages.error(request,"Please check the data you have entered.")
			return redirect('/index/')
	
	return render(request,'index.html')


	
def contact(request):
	if request.method=='POST':
		nm=request.POST['name']
		em=request.POST['email']
		txt=request.POST['text']
		try:
			conobj=Contact(name=nm,email=em,text=txt)
			conobj.save()
			return redirect('/index/')
		except:
			return redirect('/index/')
	return render(request,'index.html')

def login_call(request):
	msg=''
	if request.method=='POST':
		un=request.POST['luname']
		pwd=request.POST['lpwd']

		user=authenticate(username=un,password=pwd)
		if user:
			login(request, user)
			profileobj=UserProfile.objects.get(user__username=request.user)
			if profileobj.usertype=='user':
				return redirect('/app01/home/')

			elif profileobj.usertype=='admin':
				return redirect('/admin01/home/')
		else:
			msg='invalid username or password'
			
	return render(request,'index.html',{'msg':msg})



def logout_call(request):
	logout(request)
	return redirect('/index/')
