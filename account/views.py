from asyncio.windows_events import NULL
from email import message
from multiprocessing import context
from django.shortcuts import get_object_or_404, render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.http import urlencode
from django.contrib import messages

from account.models import User,CreateProfile
from .forms import UserForm,CreateProfileForm,ChangeForm
# Create your views here.
def register(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Your account has been created successfully! you can now login")
            return redirect(to=reverse('login'))
        else:
            return render(request,'account/register.html',{'form':form})

    elif request.method == "GET":
        form = UserForm()
        return render(request,'account/register.html',{'form':form})
    else:
        return HttpResponse("404")
    

def login_page(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username,password=password)
        # print(dir(request))
        t=User.objects.get(username = username).last_login
        print('time0',t)
        if t == None:
            if user:
                login(request,user)
                return redirect(to=reverse('createprofile'))
            #if profile(request,username):
                #return redirect(to=reverse('profile'))
        elif t != None:
            if user:
                login(request,user)
                return redirect(to=reverse('profile'))
        else:
            messages.add_message(request,messages.ERROR,"username or password is wrong!")
        # print(username,password)
    return render(request,'account/login.html',{})

@login_required
def profile(request):
    user = request.user.username
    experiences=request.user.createprofile_set.all()
    return render(request,'account/profile.html',{"experiences":experiences,'user':user})

@login_required
def change(request,id):
    if request.user.id==id:
        u=User.objects.get(id=id)
        if request.method == 'POST':
            form = ChangeForm(request.POST, request.FILES, instance=u)
            if form.is_valid():
                form.save(commit=False)
                form.user=request.user
                form.id=id
                form.save()
                return redirect(to=reverse("profile"))
        else:
            form = ChangeForm()
            return render(request,'account/change.html', {'form' : form})
    else:
        messages.add_message(request,messages.ERROR,f"You are not authorized to update")
        return redirect(reverse('profile'))

@login_required
def createprofile(request):
    id=request.user.id
    if request.method=="POST":
        form=CreateProfileForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.id=id
            form.save() 
            messages.add_message(request,messages.SUCCESS,"your profile has been saved successfully")
            return redirect(to=reverse("profile"))
    form=CreateProfileForm()
    return render (request,'account/createprofile.html',{'form':form})

@login_required
def editprofile(request,id):
    experience=CreateProfile.objects.get(id=id)
    if experience.user.id!=request.user.id:
        messages.add_message(request,messages.ERROR,f"You are not authorized to update {experience} experience!")
        return redirect(reverse('profile'))
    if request.method=="GET":
        form = CreateProfileForm(instance=experience)
        return render(request,'account/editprofile.html',{"form":form})
    elif request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.id=id
            form.save()
            messages.add_message(request,messages.SUCCESS,"your expreience has been saved successfully")
            return redirect(to=reverse("profile"))
        else:
            return render(request,'accounts/editprofile.html',{"form":form})

def profiles (request):
    profiles = CreateProfile.objects.all()
    print(profiles)
    return render(request,
                  'account/profiles.html',
                  {"profiles": profiles})

def logout_page(request):
    logout(request)
    return redirect(to=reverse('index'))