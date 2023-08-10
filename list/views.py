import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import List
from django.db import IntegrityError
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    user=request.user
    if user.is_authenticated:
        lists=List.objects.filter(user=user).all()
        serializedlists=[list.serialize() for list in lists]
        return render(request,'list/index.html',{
        'lists':serializedlists
        })
    else:
        return HttpResponseRedirect(reverse('login'))
    
def register(request):
    if request.method!='POST':
        return render(request,'list/register.html')
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password1']
    confirm=request.POST['password2']
    if password!=confirm:
        return render(request,'list/register.html',{
            'message':"passwords don't match"
        })
    try:
        user=User.objects.create_user(username,email,password)
        user.save()
    except IntegrityError:
        return render(request,'list/register.html',{
            'message':"The email or the username is already registered"
        })
    login(request,user)
    return HttpResponseRedirect(reverse('index'))

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'list/login.html',{
                'message':'Invalid password or username'
        })
    return render(request,'list/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
@csrf_exempt
def add(request):
    if request.method=='POST':
        data=json.loads(request.body)
        text=data.get('text')
        if not text:
            return JsonResponse({
                "Error":"Added empty task"
            })
        list=List(user=request.user,text=text)
        list.save()
        return JsonResponse({"message":"Successfully added"})
    lists=List.objects.all()
    serializelist=[list.serialize() for list in lists]
    return JsonResponse(serializelist,safe=False)

@login_required
@csrf_exempt
def mark(request,listid):
    if request.method=='POST':
        list=List.objects.get(pk=listid)
        list.done=True
        list.save()
        return JsonResponse({'Message':'list marked successfully'})

@login_required
@csrf_exempt
def delete_view(request,listid):
    if request.method=='POST':
        list=List.objects.get(pk=listid)
        list.delete()
        return JsonResponse({'message':'List deleted'})


        