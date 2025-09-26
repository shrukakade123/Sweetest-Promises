from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
def home(request):
    from events.models import Service, Package
    featured = Service.objects.all()[:4]
    packages = Package.objects.all()[:3]
    return render(request, 'core/home.html', {'featured': featured, 'packages': packages})
def about(request):
    return render(request, 'core/about.html')
def contact(request):
    if request.method=='POST':
        messages.success(request, 'Thanks! We received your message.')
        return redirect('core:contact')
    return render(request, 'core/contact.html')
def user_login(request):
    if request.method=='POST':
        u=request.POST.get('username'); p=request.POST.get('password')
        user=authenticate(request, username=u, password=p)
        if user: login(request,user); messages.success(request,'Logged in'); return redirect('core:home')
        messages.error(request,'Invalid credentials')
    return render(request, 'core/login.html')
def user_signup(request):
    if request.method=='POST':
        u=request.POST.get('username'); e=request.POST.get('email'); p=request.POST.get('password')
        if User.objects.filter(username=u).exists():
            messages.error(request,'Username exists')
        else:
            user=User.objects.create_user(username=u,email=e,password=p); login(request,user); messages.success(request,'Account created'); return redirect('core:home')
    return render(request, 'core/signup.html')
def user_logout(request):
    logout(request); messages.info(request,'Logged out'); return redirect('core:home')
