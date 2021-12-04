from django.shortcuts import render,redirect
from .models import religion,city,lang,story
from perfectshadi.models import UserProfile,Contact
from app01.models import UserData
from perfectshadi.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def home(request):
	uobj=UserProfile.objects.get(user__username=request.user)
	count=UserProfile.objects.all().count()
	active=UserData.objects.all().count()
	users=User.objects.all()
	return render(request,'adminhome.html',{'count':count,'active':active,'users':users})


def add_religion(request):
	relobjs=religion.objects.all()
	if request.method=='POST':
		reli=request.POST['rel']
		relobj=religion(religioame=reli)
		relobj.save()

		
	return render(request,'addrel.html',{'relobjs':relobjs})


@login_required	
def del_rel(request,id):
	robj=religion.objects.get(id=id)
	robj.delete()
	return redirect('/admin01/religion/')

@login_required
def add_city(request):
	ciobjs=city.objects.all()
	if request.method=='POST':
		addcity=request.POST['cit']
		cobj=city(cityname=addcity)
		cobj.save()
	return render(request,'addcity.html',{'ciobjs':ciobjs})


@login_required
def add_lang(request):
	langobjs=lang.objects.all()
	if request.method=='POST':
		l=request.POST['mt']
		lobj=lang(mothertongue=l)
		lobj.save()
	return render(request,'addlang.html',{'langobjs':langobjs})


@login_required
def admin_sign(request):
	if request.method=="POST":
		fname=request.POST['fname']
		lname=request.POST['lname']
		uname=request.POST['uname']
		email=request.POST['email']
		mobile=request.POST['mobile']
		dob=request.POST['dob']
		utype=request.POST['utype']
		pwd=request.POST['pwd']

		uobj=User(first_name=fname,last_name=lname,username=uname,password=make_password(pwd),email=email)
		uobj.save()

		u_profile=UserProfile(user=uobj,dob=dob,usertype=utype,mobile=mobile)
		u_profile.save()
		return redirect('/admin01/admin_sign/')

	return render(request,'adminsignup.html')

def view_fbk(request):
	fbk=[]
	cnobj=Contact.objects.all()
	for i in cnobj:
		fbk.append(i)
	return render(request,'view_fbk.html',{'fbk':fbk})

def add_story(request):
	stry=[]
	sobj=story.objects.all()
	for i in sobj:
		stry.append(i)
	if request.method=='POST':
		pic=request.FILES['img']
		bname=request.POST['bride']
		bgname=request.POST['bridegroom']
		stry=request.POST['story']
		try:
			sobj=story(img=pic,bride=bname,bridegroom=bgname,story=stry)
			sobj.save()
			return redirect('/admin01/add_story/')
		except:
			return redirect('/admin01/add_story/')
	return render(request,'story.html',{'stry':stry})

@login_required	
def del_story(request,id):
	sobj=story.objects.get(id=id)
	sobj.delete()
	return redirect('/admin01/add_story/')


