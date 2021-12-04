from django.shortcuts import render
from perfectshadi.models import UserProfile
from admin01.models import religion,city,lang
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	uobj=UserProfile.objects.get(user__username=request.user)
	return render(request,'userhome.html',{'uobj':uobj})
def myprofile(request):
	relobjs=religion.objects.all()
	ciobjs=city.objects.all()
	uobj=UserProfile.objects.get(user__username=request.user)
	uprofile=UserProfile.objects.filter(user_id=uobj.id)
	items = []
	for i in uprofile:
		items.append(UserProfile.objects.get(id=i.user_id))
		d=str(i.dob)
		o=d.replace(',','')
		dob=o[0:10]
		print(dob)
	if request.methods=="Post":
		pic=request.FILES['pic']
		faname=request.POST['faname']
		mname=request.POST['mname']
		gender=request.POST['gender']
		mstatus=request.POST['mstatus']
		height=request.POST['height']
		profession=request.POST['profession']
		quali=request.POST['quali']
		religion=request.POST['rel']
		mtongue=request.POST['mtongue']
		ciname=request.POST['city']
		dist=request.POST['dist']
		pin=request.POST['pin']
		hobbies=request.POST['hob']



	return render(request, 'myprofile.html',{'items':items,'dob':dob,'relobjs':relobjs,'ciobjs':ciobjs})