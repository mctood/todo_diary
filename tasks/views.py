from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'tasks/active.html')


def done(request):
    return render(request, 'tasks/done.html')