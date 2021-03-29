from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateQuestboardForm, CreateQuestForm
from .models import Questboard, Quest
from django.contrib.auth.models import User


def home_view(request):
	questboards = Questboard.objects.all().order_by('-id')
	context = {'questboards': questboards}
	return render(request, 'questboard/home.html', context)


def questboard_detail_view(request, pk):
	questboard = Questboard.objects.get(id=pk)
	teacher = User.objects.get(id=questboard.creator_id)
	context = {'questboard': questboard, 'teacher': teacher}
	return render(request, 'questboard/questboard_detail.html', context)
	
	
@login_required(login_url='login')
def create_quest(request, pk):
	questboard = Questboard.objects.get(id=pk)
	teacher = User.objects.get(id=questboard.creator_id)

	if request.method == 'POST':
		form = CreateQuestForm(request.POST)
		if form.is_valid():
			return redirect('home')
	else: 
		form = CreateQuestForm()
		
	context = {'form': form, 'questboard': questboard, 'teacher': teacher}
	return render(request, 'questboard/create_quest.html', context)
	
	
	
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
	
	
@login_required(login_url='login')
def create_questboard(request):
	if request.method == 'POST':
		form = CreateQuestboardForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.creator = request.user
			obj.save()
			return redirect('home')
	else: 
		form = CreateQuestboardForm()
		
	return render(request, 'questboard/create_questboard.html', {'form': form})