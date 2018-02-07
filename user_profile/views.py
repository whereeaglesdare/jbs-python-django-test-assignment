from django.shortcuts import render
from django.contrib.auth.models import User

from .models import UserProfile

def index(request):
    user = User.objects.filter(username='admin').values('first_name', 'last_name')[0]
    user.update(UserProfile.objects.filter(user__username='admin').values()[0])
    return render(request, 'user_profile/index.html', user)