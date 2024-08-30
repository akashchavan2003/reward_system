from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from admin_app import models

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff: 
                print(request.user.id)
                return redirect('admin_dash', id=request.user.id)
            else:
                return redirect('user_dash',id=request.user.id)
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    
    return render(request, 'login.html')

from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404,redirect


def register_admin(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password=request.POST.get('password')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name=request.POST.get('name')
            user.is_staff=True
            user.save()
            print("user creted successfully")
            return render(request,'admin_signup.html',{'error_message':f"Account created successfully with username:{user.first_name}"})                        
    except Exception as e:
        print("Account created failed due to:",e)
        return render(request,'admin_signup.html',{'error_message':"Account created Failed"})

    return render(request,'admin_signup.html')




def register_user(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password=request.POST.get('password')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name=request.POST.get('name')
            profile_picture = request.FILES.get('profile_picture')

            user.is_staff
            user.save()
            return render(request,'user_signup.html',{'error_message':f"Account created successfully with username:{user.first_name}"})   
                         
    except Exception as e:
        print("account creation failed due to:",e)
        return render(request,'user_signup.html',{'error_message':"Account created Failed"})

    return render(request,'user_signup.html')



def admin_dash_view(request,id):
    try:
        admin_taks_obj=models.AdminTask.objects.filter(user_id=id)
        print(admin_taks_obj.app_name)
    except Exception as e:
        print(e)
    return render(request,'admin_dashboard.html',{'apps':admin_taks_obj})

