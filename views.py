from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse


def homes(request):
    return render(request, 'homes.html') #Main Page

def signups(request):
    if request.method=='POST':
        fname=request.POST.get('fullname')
        uname=request.POST.get('username')
        faname=request.POST.get('Fathername')
        email=request.POST.get('email')
        cnumb=request.POST.get('contactNumber')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirmPassword')

        if pass1!=pass2:
            return ("Your password doesn't match.")
        my_user=User.objects.create_user(fname,uname,faname,email,cnumb,pass1,pass2)
        my_user.save()
        return redirect('logins')
        print(fname,uname,faname,email,cnumb,pass1,pass2)
    return render(request, 'signups.html')

def admin(request):
    return render(request, 'admin.html')

def logins(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'url': '/dashboard'})
        else:
            return JsonResponse({'status': 'failed', 'message': 'Login failed. Please check your credentials.'})
     else:
        return render(request, 'login.html')  # Render the login page

def dashboard(request):
    return render(request, 'dashboard.html')

def election(request):
    return render(request, 'election.html')


def voter(request):
    return render(request, 'voter.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def terms(request):
    return render(request, 'terms.html')

def steps(request):
    return render(request, 'steps.html')

def profile(request):
    return render(request, 'profile.html')