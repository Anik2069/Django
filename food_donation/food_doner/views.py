from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Doner_Post
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.
def home(request):
    context = {
        'posts' : Doner_Post.objects.all()
    }
    return render(request,'food_doner/home.html', context);
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'You Account has been created! Your are now able to login!!')
            return redirect('food_donation')
    else:
        form = UserRegisterForm()
    return  render(request,'food_doner/register.html',{'form': form});