from django.shortcuts import render,redirect
from perfectshadi.models import UserProfile
from admin01.models import religion,city,lang
from django.contrib.auth.models import User
from .models import UserData,Age
from django.contrib import messages
import datetime
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):

	m=[]

	profile=[]
	ageobjs=Age.objects.all()
	
	relobjs=religion.objects.all()
	usobj=UserData.objects.all()
	uobj = UserProfile.objects.get(user__username=request.user)
	
	userdata=UserData.objects.filter(user_id=uobj.id)

	for i in userdata:
		profile.append(i)
		if i.gender=='female':
			for x in usobj:
				if x.gender=='male':
					m.append(x)
					m.reverse()
		elif i.gender=='male':
			for y in usobj:
				if y.gender=='female':
					m.append(y)
					m.reverse()
	return render(request,'userhome.html',{'m':m,'relobjs':relobjs,'profile':profile})


@login_required
def myprofile(request):

	relobjs=religion.objects.all()
	ciobjs=city.objects.all()
	mt=lang.objects.all()
	uobj=UserProfile.objects.get(user__username=request.user)
	uprofile=UserProfile.objects.filter(user_id=uobj.id)
	userdata=UserData.objects.filter(user_id=uobj.id)
	print(userdata)
	print(uobj)

	udata=[]
	for j in userdata:
		udata.append(UserData.objects.get(user_id=j.user_id))

	items = []
	
	for i in uprofile:
		items.append(UserProfile.objects.get(id=i.user_id))
		
		
	return render(request, 'myprofile.html',{'udata':udata,'items':items,'relobjs':relobjs,'ciobjs':ciobjs,'mt':mt})



@login_required
def add_data(request):
	uobj=UserProfile.objects.get(user__username=request.user)
	
	userdata=UserProfile.objects.filter(user_id=uobj.id)
	mage=[]
	da= UserProfile.objects.filter(id=uobj.id)
	for i in da:
		db=str(i.dob)
		db1=db.replace('-',"")
		db2=db1[0:4]
		db3=int(db2)
	d=datetime.date.today()
	s1=str(d)
	s2=s1.replace('-',"")
	s3=s2[0:4]
	s4=int(s3)
	ag=s4-db3
	mage.append(ag)
	#print(mage)

	
	
	msgs=[]
	relobjs=religion.objects.all()
	ciobjs=city.objects.all()
	mt=lang.objects.all()
	if request.method=="POST":
		pic=request.FILES['pic']
		fn=request.POST['fn']
		ln=request.POST['ln']
		faname=request.POST['faname']
		mname=request.POST['mname']
		gender=request.POST['gender']
		mstatus=request.POST['mstatus']
		height=request.POST['height']
		profession=request.POST['profession']
		quali=request.POST['quali']
		relig=request.POST['rel']
		mtongue=request.POST['mtongue']
		ciname=request.POST['city']
		dist=request.POST['dist']
		pin=request.POST['pin']
		hobbies=request.POST['hob']
		age=request.POST['ag']

		try:
			dataobj=UserData(user=uobj,pic=pic,First_name=fn,Last_name=ln,faname=faname,mname=mname,gender=gender,mstatus=mstatus,height=height,profession=profession,qualification=quali,religion=relig,mothertongue=mtongue,cityname=ciname,dist=dist,pin=pin,hobbies=hobbies,age=age)
			dataobj.save()
			messages.success(request, "Your Profile is completed!")
			return redirect("/app01/add_data/")
		except:
			messages.error(request,"Please provide correct details! take care of mandatory fields!")
			return redirect("app01/add_data/")

	return render(request, 'userdata.html',{'relobjs':relobjs,'ciobjs':ciobjs,'mt':mt,'mage':mage})



@login_required
def update_details(request):
	relobjs=religion.objects.all()
	ciobjs=city.objects.all()
	mt=lang.objects.all()
	uobj=UserProfile.objects.get(user__username=request.user)
	uprofile=UserProfile.objects.filter(user_id=uobj.id)
	userdata=UserData.objects.filter(user_id=uobj.id)
	print(userdata)
	print(uobj)

	udata=[]
	for j in userdata:
		udata.append(UserData.objects.get(user_id=j.user_id))

	items = []
	
	for i in uprofile:
		items.append(UserProfile.objects.get(id=i.user_id))
	
	
	print(uobj)
	relobjs=religion.objects.all()
	ciobjs=city.objects.all()
	mt=lang.objects.all()
	if request.method=="POST":
		pic=request.FILES['pic']
		faname=request.POST['faname']
		mname=request.POST['mname']
		gender=request.POST['gender']
		mstatus=request.POST['mstatus']
		height=request.POST['height']
		profession=request.POST['profession']
		quali=request.POST['quali']
		relig=request.POST['rel']
		mtongue=request.POST['mtongue']
		ciname=request.POST['city']
		dist=request.POST['dist']
		pin=request.POST['pin']
		hobbies=request.POST['hob']
		dataobj=UserData.objects.filter(id=id)
		dataobj.Update(user=uobj,pic=pic,faname=faname,mname=mname,gender=gender,mstatus=mstatus,height=height,profession=profession,qualification=quali,religion=relig,mothertongue=mtongue,cityname=ciname,dist=dist,pin=pin,hobbies=hobbies)
		return redirect("/app/myprofile/")

	return render(request, 'update.html',{'udata':udata,'relobjs':relobjs,'ciobjs':ciobjs,'mt':mt})

@login_required
def show(request,id):
	gdata=UserData.objects.filter(user_id=id)
	pro_data=[]
	for i in gdata:
		pro_data.append(i)
		print(pro_data)
	return render(request,'showprofile.html',{'pro_data':pro_data})


@login_required
def update_pro(request,id):
	userdata=UserData.objects.get(user_id=id)
	relobjs=religion.objects.all()
	ciobjs=city.objects.all()
	mt=lang.objects.all()
	uobj=UserProfile.objects.get(user__username=request.user)
	uprofile=UserProfile.objects.filter(user_id=uobj.id)
	userdata=UserData.objects.filter(user_id=uobj.id)
	print(userdata)
	print(uobj)

	udata=[]
	for j in userdata:
		udata.append(UserData.objects.get(user_id=j.user_id))

	items = []
	
	for i in uprofile:
		items.append(UserProfile.objects.get(id=i.user_id))
	
	
	print(uobj)
	relobjs=religion.objects.all()
	ciobjs=city.objects.all()
	mt=lang.objects.all()
	if request.method=="POST":
		faname=request.POST['faname']
		mname=request.POST['mname']
		gender=request.POST['gender']
		mstatus=request.POST['mstatus']
		height=request.POST['height']
		profession=request.POST['profession']
		quali=request.POST['quali']
		relig=request.POST['rel']
		mtongue=request.POST['mtongue']
		ciname=request.POST['city']
		dist=request.POST['dist']
		pin=request.POST['pin']
		hobbies=request.POST['hob']

		dataobj=UserData.objects.filter(user_id=id)
		dataobj.update(user=uobj,faname=faname,mname=mname,gender=gender,mstatus=mstatus,height=height,profession=profession,qualification=quali,religion=relig,mothertongue=mtongue,cityname=ciname,dist=dist,pin=pin,hobbies=hobbies)
		

		return redirect("/app01/myprofile/")


	return render(request, 'update.html',{'udata':udata,'relobjs':relobjs,'ciobjs':ciobjs,'mt':mt})



@login_required
def cat_search(request,name):
	m=[]
	profile=[]
	relobjs=religion.objects.all()
	uobj = UserProfile.objects.get(user__username=request.user)
	usobj=UserData.objects.all()
	userdata=UserData.objects.filter(user_id=uobj.id)

	for i in userdata:
		profile.append(i)
		if i.gender=='female':
			for x in usobj:
				if x.gender=='male' and x.religion==name:
					m.append(x)
		elif i.gender=='male':
			for y in usobj:
				if y.gender=='female' and y.religion==name:
					m.append(y)
	
	return render(request,'cat_search.html',{'m':m,'relobjs':relobjs,'profile':profile})



@login_required
def chnge_passwd(request):
	uobj=UserProfile.objects.get(user__username=request.user)
	uprofile=User.objects.filter(id=uobj.user_id)
	for i in uprofile:
		print(i.password)
		print(i.username)

	if request.method=='POST':
		passwd=request.POST['pwd']
		npasswd=request.POST['npw']
		
	user=authenticate(username=i.username,password=passwd)
	if user:
		uprofile.update(password=make_password(npasswd))
		messages.success(request,'Password Updated Successfully!!')
		return redirect('/index/')

	else:
		messages.error(request,'invalid password!')
	return render(request,'userhome.html')

@login_required
def deactivate(request):
	uobj=UserProfile.objects.get(user__username=request.user)
	usdata=UserData.objects.filter(user_id=uobj.id)
	usdata.delete()
	return redirect('/index/')


@login_required
def search1(request):
	s=[]
	profile=[]
	usobj=UserData.objects.all()
	relobjs=religion.objects.all()
	uobj = UserProfile.objects.get(user__username=request.user)
	userdata=UserData.objects.filter(user_id=uobj.id)

	for i in userdata:
		profile.append(i)
	if request.method=='POST':
		key=request.POST['search']
		for i in usobj:
			if key.lower() in i.First_name or key.capitalize() in i.First_name:
				s.append(i)
		return render(request,'search.html',{'s':s,'profile':profile,'relobjs':relobjs})

	return render(request,'userhome.html')


		


	