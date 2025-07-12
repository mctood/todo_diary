from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from tasks.models import Task

@method_decorator(csrf_exempt)
def common_put(self, request):
    task = Task.objects.get(id=request.POST['id'])
    task.done = bool(int(request.POST['checked']))
    task.checked_at = timezone.now()
    task.save()
    return JsonResponse({'ok': True})

class TasksAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.filter(
            user=request.user,
            done=False,
        ).order_by('-checked_at')
        return render(request, 'tasks/active.html', {
            "tasks": tasks,
        })

    def post(self, request):
        task = Task.objects.create(
            title=request.POST['task'],
            user=request.user,
        )
        return JsonResponse({'ok': True, 'id': task.id})

    put = common_put




class TasksDoneAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.filter(
            user=request.user,
            done=True,
        ).order_by('-checked_at')
        return render(request, 'tasks/done.html', {
            "tasks": tasks,
        })

    put = common_put
