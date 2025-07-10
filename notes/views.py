from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'notes/today.html')


def archive(request):
    return render(request, 'notes/archive.html')