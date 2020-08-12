from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Doner_Post
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance= request.user)
        p_form=  ProfileUpdateForm(request.POST,request.FILES,instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You Account has been updated!!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form' : p_form
    }
    return  render(request,'food_doner/profile.html',context);
