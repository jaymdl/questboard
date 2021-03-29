from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages 


def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Thanks for signing up! ' + username   +'! ')
			login(request, user)
			# log the user in
			return redirect("home")
	else: 
		form = UserCreationForm()
	return render(request, 'questboard/signup.html', {'form': form})
	
