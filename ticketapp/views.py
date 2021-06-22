from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Movie, Halls, Userdata


def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		if username == "" or password == "" or email == "":
			messages.info(request, 'Please fill the required fields')
			return redirect('/')
		if User.objects.filter(username=username).exists():
			messages.info(request, 'This username is not available')
			return redirect('/')
		elif User.objects.filter(email=email).exists():
			messages.info(request, 'This email is already taken!')
			return redirect('/')
		else:
			user = User.objects.create_user(username=username, password=password, email=email)
			user.save()
			user = Userdata(username=username, email=email)
			user.save()
			return redirect('/')

	else:
		return render(request, 'index.html')


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'invalid credentials')
			return redirect('/')
	return render(request, 'login.html')


def logout(request):
	auth.logout(request)
	return redirect('/')


def index(request):
	return render(request, 'index.html')


def movies(request):
	movies=Movie.objects.all()
	params = {'movie': movies}
	return render(request, 'movies.html', params)


def halls(request):
	cinms = Halls.objects.all()
	params = {'cinema': cinms}
	return render(request, 'cinemas.html', params)


def detail(request, item):
	show=Movie.objects.get(id = item)
	params = {'dets':show}
	return render(request, 'details.html', params)


def mysaved(request):
	user = Userdata.objects.get(username = request.user.username)
	x = user.username
	y = user.email
	z = user.transaction
	p = user.choice.all()
	params = { 'x':x,
			   'y':y,
	           'z':z,
			   'p':p,}
	return render(request, 'saved.html', params)


def book(request, item):
	user = Userdata.objects.get(username = request.user.username)
	movie = Movie.objects.get(id = item)
	Userdata.objects.filter(username = user.username).update(transaction = user.transaction + movie.Price)
	user.choice.add(movie)
	messages.info(request, "Congratulations!!!! Be prepare with your popcorn and cold drinks")
	return redirect('/movies')