from django.shortcuts import render
from models import Person, Image
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.
def home(request):
	image_list = Image.objects.all()

	return render(request, 'home.html', {
			'image_list': image_list,
			
		
			 })

def base(request):
	return render(request, 'base.html', {'key': "value" })



def auth(request):

	
	pwd = request.POST.get('Password','')
	usern = request.POST.get('Username','')

	user = authenticate(username=usern, password=pwd)
	print usern
	print pwd

	
	if user is not None:
		login(request, user)
		u = user
		return HttpResponseRedirect("/")
	else:
		return render(request, 'sssss.html', {'key': "value" })

# def loggedin(request):
# 	return render_to_response(request, 'home.html', {'user': request.user.username })

def log_out(request):
	logout(request)
	return HttpResponseRedirect("/")

