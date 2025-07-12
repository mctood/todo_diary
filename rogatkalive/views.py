import random
import re

from django.contrib import auth
from django.shortcuts import render, redirect

from rogatkalive.rofl_nicks import rofl_nicks
from rogatkalive.models import User


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def trust(request):
    return render(request, 'main/trust.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        user_exists = User.objects.filter(username=request.POST['username']).exists()
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            error = "Что-то из этого неверно"
            if user_exists:
                random_nick = random.choice(rofl_nicks)
                error = f"Этот пароль принадлежит пользователю {random_nick}, но уж никак не вам."
                request.session['rofl_nick'] = random_nick
            if request.POST['username'] == request.session['rofl_nick']:
                error = "Я пошутил."
                del request.session['rofl_nick']
            return render(request, 'main/login.html', {
                "ok": False,
                "error": error,
                "creds": {
                    "username": request.POST['username'],
                    "password": request.POST['password']
                }
            })
    return render(request, 'main/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def me(request):
    return render(request, 'main/me.html')


def register(request):
    if request.method == 'POST':
        if (result := clean_register(request.POST))['ok']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                name=request.POST['name']
            )
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'main/register.html', result)
    return render(request, 'main/register.html')


def create_key(request):
    return render(
        request, 'main/create_key.html'
    )


def clean_register(post: dict):
    error = None
    if len(post['username']) < 4:
        error = "Имя пользователя слишком короткое 🍆"
    if len(post['password']) < 8:
        error = f"Добавьте ещё " + str(8 - len(post['password'])) + number_format(
            8 - len(post['password']),
            " символ"
        ) + " к вашему паролю"
    if len(post['name']) < 1:
        error = "Пустое имя? Вы серьёзно?"

    if re.match(r"[^a-zA-Z0-9.]", post['username']):
        error = "В имени пользователя обнаружены странные символы"
    if User.objects.filter(username=post['username']).exists():
        error = "Это имя пользователя уже забрали"

    return {
        "ok": not bool(error),
        "error": error,
    }


def number_format(number: int, base: str):
    fin = ""
    if 10 <= number <= 20 or 5 <= number % 10 <= 9:
        fin = "ов"
    elif 2 <= number % 10 <= 4:
        fin = "а"

    return base + fin