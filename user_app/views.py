from admin_app import models
from .models import UserTask,UserProfile
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


def user_dash_view(request,id):
    points=0
    try:
        try:
            po=UserProfile.objects.get(user_id=id)
            points=po.points_earned

        except Exception as e:
            print(e)
        obj=models.AdminTask.objects.all()
        user_details=User.objects.get(id=id)
        task_done=UserTask.objects.filter(user_id=id)
    except Exception as e:
        print(e)
    return render(request,'user_dashboard.html',{'available_tasks':obj,'user':user_details,'done_task':task_done,'points_earned':points})
 

from .models import UserTask, UserProfile, User

def download_done(request, id, user_id, points):
    if request.method == 'POST':
        user_instance = get_object_or_404(User, id=user_id)
        screenshot = request.FILES.get('file')

        if not screenshot:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        chk = UserTask.objects.filter(admin_task_id=id, user=user_instance)
        if chk.exists():
            return JsonResponse({'error': 'Task already completed'}, status=400)

        try:
            UserTask.objects.create(
                screenshot=screenshot,
                admin_task_id=id,
                user=user_instance,
                points=points
            )

            user_profile, created = UserProfile.objects.get_or_create(user=user_instance)
            user_profile.points_earned += points
            user_profile.task_completed += 1
            user_profile.save()

            return JsonResponse({'success': 'Task completed successfully'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
