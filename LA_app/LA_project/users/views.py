from django.shortcuts import render
from .models import Profiles

def profiles(request):
    profiles = Profiles.objects.all()
    return render(request, 'users/profiles.html', {'profiles': profiles})

def userProfile(request, pk):
    profile = Profiles.objects.get(id=pk)
    return render(request, 'users/user-profile.html', {'profile': profile})
