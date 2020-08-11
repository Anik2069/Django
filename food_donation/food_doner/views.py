from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Doner_Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def home(request):
    context = {
        'posts' : Doner_Post.objects.all()
    }

    return render(request,'food_doner/home.html', context);
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created for {username}!!')
            return redirect('food_donation')
    else:
        form = UserCreationForm()


    return  render(request,'food_doner/register.html',{'form': form});