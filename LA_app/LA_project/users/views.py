from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm  # custom form below
from .forms import CustomUserCreationForm
from .models import Profiles, User

def profiles(request):
    profiles = Profiles.objects.all()
    return render(request, 'users/profiles.html', {'profiles': profiles})

def userProfile(request, pk):
    profile = Profiles.objects.get(id=pk)
    return render(request, 'users/user-profile.html', {'profile': profile})

def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')


    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['password']
        print(request.POST)
        
        try:
            user = User.objects.get(username=uname)
        except:
            messages.error(request, 'Username not Found')
            print('Username not Found.')
        
        user = authenticate(request, username=uname, password=upass)

        if user:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Username or Password not Found")
            print('Username or Password not Found')

    return render(request, 'users/login_registration.html', {'page': 'login'})

def registerUser(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Registration Complete')
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, 'Please Provide Data Properly.')
    # form = UserCreationForm()
    return render(request, 'users/login_registration.html', {'page': 'register', 'form': CustomUserCreationForm()})

def logoutUser(request):
    logout(request)
    return redirect('login')