from .models import AdminTask
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def add_app_view(request):
    user=request.user.id
    app=AdminTask.objects.filter(user_id=user)
    
    try:
        if request.method == 'POST':
                
                app_name= request.POST.get('name')
                descrption=request.POST.get('description')
                url=request.POST.get('download_url')
                points=request.POST.get('points')
                pbj=AdminTask.objects.create(
                    user=request.user,
                    app_name=app_name,
                    task_description=descrption,
                    link=url,
                    points=points
                )
                pbj.save()
                return render(request,'admin_dashboard.html',{'error_message':"App Added successfully...."})
    except Exception as e:
        print("Adding failed due to", e)
        return render(request,'admin_dashboard.html',{'error_message':"App Adding Failed..."})
    return render(request,'admin_dashboard.html',{'app':app})

from django.contrib.auth import logout
def logout_view(request):
     logout(request)
     return render(request,'login.html')




def edit_app(request,id):
     pass



def delete_app(request):
     pass
