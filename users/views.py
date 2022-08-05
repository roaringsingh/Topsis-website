from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.core import exceptions

from topsis.models import UserData
from .forms import UserRegistrationForm
from .mails import send_mail


# Create your views here.

def home_view(request):
    context = {
    }
    return render(request, 'users/home.html', context)


def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Hi, {username} your account was created')
        return redirect('home')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required()
def profile_view(request):
    if request.POST:
        request.user.email = request.POST.get('email')
        request.user.save()
    data = UserData.objects.filter(user=request.user)
    if not data:
        messages.info(request, 'No data to show')
    context = {
        'data': data
    }
    return render(request, 'users/profile.html', context)


@login_required()
def delete_account_view(request):
    print(request.user, 'login')
    try:
        obj = User.objects.get(username=request.user)
        obj.delete()
        messages.success(request, 'Your Account was deleted successfully')
        return redirect('login')
    except exceptions.ObjectDoesNotExist:
        messages.warning(request, 'Account does not exist')
        return redirect('login')


@login_required()
def send_mail_view(request, key):
    print(request.user, 'send mail', key)
    obj = UserData.objects.filter(user=request.user).get(id=key)
    if obj.file and request.user.email:
        send_mail(obj.file, request.user)
        messages.success(request, f'Hi, {request.user} your mail was sent')
        return redirect('profile')
    messages.warning(request, f'Hi, {request.user} your mail was not sent')
    return redirect('profile')


@login_required()
def delete_record_view(request, key):
    print(request.user, 'delete', key)
    try:
        obj = UserData.objects.filter(user=request.user).get(id=key)
        obj.delete()
        messages.success(request, f'Hi, {request.user} Record {key} was deleted.')
        return redirect('profile')
    except exceptions.ObjectDoesNotExist:
        messages.warning(request, f'Hi, {request.user} Record {key} does not exist.')
        return redirect('profile')
