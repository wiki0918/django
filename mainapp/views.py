from django.shortcuts import render,redirect
from django.http import HttpResponse
from mainapp.models import User
from recipe.models import Recipe

import time
now = time.strftime("%Y-%m-%d", time.localtime())

# Create your views here.
def get_index(request):
    title = '2018 Best Car'
    email = request.session.get('email','')    
    recipes = Recipe.objects.all()

    return render(request,'index.html',locals())

def get_user(request):
    
    return render(request,'user.html',locals())

def update_user(request):
    username = request.POST.get('username','')
    uid = request.POST.get('uid','')
    if uid :
        user = User.objects.filter(uid=uid)
        user.update(username=username)
    return redirect('/')

def post_login(request):
    email = request.POST['email'] 
    password = request.POST['password']
    
    user = User.objects.filter(email=email,password=password)

    if user :
        request.session['email'] = email
        return redirect('/')
    else:
        return redirect('/')

def post_logout(request):

    del request.session['email']
    return redirect('/')

def post_signup(request):
    email = request.POST['email'] 
    password = request.POST['password']
    
    user = User.objects.filter(email=email)
    
    if user :
        return redirect('/signup')
    else:
        User.objects.create(email=email,password=password,create_time=now)
        return redirect('/')

def get_signup(request):
    return render(request,'signup.html')

def set_cookie(request):
    response = HttpResponse('set_cookie')
    response.set_cookie('lucky_number',8)
    return response

def get_cookie(request):
    if 'lucky_number' in request.COOKIES:
        return HttpResponse('Your lucky_number is {0}'.format(request.COOKIES['lucky_number']))
    else:
        return HttpResponse('No cookies.') 
    
def set_session(request):
    request.session['age'] = 100
    return HttpResponse('set_session')  

def get_session(request):
    response = request.session.get('email','')
    return HttpResponse(response) 