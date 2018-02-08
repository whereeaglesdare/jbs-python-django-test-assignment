from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import UserForm, ProfileForm


def index(request):
    user = User.objects.filter(username='admin').values('first_name', 'last_name')[0]
    user.update(UserProfile.objects.filter(user__username='admin').values()[0])
    return render(request, 'user_profile/index.html', user)


@login_required
def edit_user(request):
    user = User.objects.get(username='admin')
    user_profile = UserProfile.objects.get(user=user)
    user_form = UserForm(instance=user)
    profile_form = ProfileForm(instance=user_profile)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
    return render(request, 'user_profile/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })