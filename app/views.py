from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.http import HttpResponse
import datetime
from app.models import *
import uuid

def index(request):
	try:
		email = request.session['useremail']
		return redirect('/dash/')	
	except:
		dic={
			'login':'block',
			'create':'none',
			'verify':'none'
			}
		return render(request, 'index.html', dic)

def otp(request):
	dic={
		'login':'none',
		'create':'none',
		'verify':'block'
		}
	return render(request, 'index.html', dic)

@csrf_exempt
def create(request):
	if request.method=='POST':
		name=request.POST.get('name2')
		email=request.POST.get('email2')
		password=request.POST.get('password2')
		UserData.objects.filter(email=email).delete()
		if UserData.objects.filter(email=email).exists():
			return HttpResponse("<script>alert('Account Already Exists');window.location.replace('/index/')</script>")
		else:
			UserData(email=email, name=name, password=password).save()
			otp=uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today())+name+password+email).int
			otp=str(otp)
			otp=otp.upper()[0:6]
			msg='''Hi there!
Your One Time Password is,

'''+otp+'''

Thanks!'''
			sub='IDE Email Verification'
			e=EmailMessage(sub,msg,to=[email])
			e.send()
			request.session['OTP'] = otp
			request.session['email'] = email
			dic={
				'login':'none',
				'create':'none',
				'verify':'block',
				'email':email
				}
			return render(request, 'index.html', dic)

@csrf_exempt
def verify(request):
	if request.method=='POST':
		email=request.session['email']
		otp=request.session['OTP']
		otp2=request.POST.get('otp')
		if otp==otp2:
			request.session['useremail'] = email
			return redirect('/dash/')
		else:
			return HttpResponse("<script>alert('Incorrect OTP');window.location.replace('/otp/')</script>")

def dash(request):
	try:
		email=request.session['useremail']
		user = UserData.objects.filter(email=email)[0]
		dic={'name':user.name}
		return render(request, 'dash.html', dic)
	except:
		return redirect('/index/')

@csrf_exempt
def checklogin(request):
	if request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('password')
		if UserData.objects.filter(email=email, password=password).exists():
			request.session['useremail'] = email
			return redirect('/dash/')
		else:
			return HttpResponse("<script>alert('Incorrect Email or Password');window.location.replace('/index/')</script>")

def logout(request):
	try:
		del request.session['useremail']
		return redirect('/index/')
	except:
		return redirect('/index/')

def pythonide(request):
	return render(request, 'pythonide.html', {})