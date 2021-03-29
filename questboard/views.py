from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def home_view(request):
	return render(request,'questboard/home.html')
	
	
def signup_view(request):
	if request.user.is_authenticated:
		return redirect("home")
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Thanks for signing up, ' + username   +'! ')
			login(request, user)
			# log the user in
			return redirect("home")
	else:
		form = UserCreationForm()
	return render(request, 'questboard/signup.html', {'form': form})
	

def login_view(request):
	if request.user.is_authenticated:
		return redirect("home")
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# login the user
			user = form.get_user()
			login(request, user)
			return redirect("home")
	else: 
		form = AuthenticationForm()
	return render(request, 'questboard/login.html', {'form': form})
	

def logout_view(request):
	logout(request)
	return redirect("home")


def teacher_homepage_view(request):
	return HttpResponse("Teacher homepage.")