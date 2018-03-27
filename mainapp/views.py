from django.shortcuts import render
from django.http import HttpResponse
from recipe.models import Recipe
# Create your views here.
def get_index(request):
    title = '2018 Best Car'
    recipes = Recipe.objects.all()
    return render(request,'index.html',locals())

def get_signup(request):
    return render(request,'signup.html')

def post_signup(request):
    email = request.POST['email'] 
    password = request.POST['password'] 
#    return render(request,'signup.html')
    return HttpResponse(email,password) 

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
    response = request.session['age']
    return HttpResponse(response) 