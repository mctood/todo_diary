import datetime
from calendar import monthrange
from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView

from notes.models import Note

MONTHS = [
    "Январь",
    "Февраль",
    "Март",
    "Апрель",
    "Май",
    "Июнь",
    "Июль",
    "Август",
    "Сентябрь",
    "Октябрь",
    "Ноябрь",
    "Декабрь",
]


class NotesAPIView(APIView):
    def get(self, request):
        note = Note.objects.filter(
            user=request.user,
            date=timezone.now().date()
        ).first()
        return render(request, 'notes/today.html', {
            "note": note,
            "date": timezone.now().date(),
        })

    def post(self, request):
        note = Note.objects.filter(
            user=request.user,
            date=timezone.now().date()
        ).first()
        if note:
            note.content = request.POST['note']
            note.mood = request.POST['mood']
            note.save()
        else:
            Note.objects.create(
                user=request.user,
                date=timezone.now().date(),
                content=request.POST['note'],
                mood=request.POST['mood']
            )
        return redirect("notes-index")


def archive(request):
    year = int(request.GET["year"]) if "year" in request.GET else timezone.now().year
    month = int(request.GET["month"]) if "month" in request.GET else timezone.now().month
    print(year, month)

    days = []
    total_days = monthrange(year, month)

    for day in range(1, total_days[1] + 1):
        daily_note = Note.objects.filter(
            date__day=day,
            user=request.user,
            date__year=year,
            date__month=month,
        ).first()
        classes = []

        if day % 7 in (6, 0):
            classes.append("weekend")
        if datetime.date(year, month, day) == timezone.now().date():
            classes.append("today")
        if datetime.date(year, month, day) <= timezone.now().date():
            classes.append("passed")
        if daily_note:
            classes.append("indicator")
            classes.append("mood-" + daily_note.mood)

        mood_icon = ""
        if daily_note:
            match daily_note.mood:
                case "1":
                    mood_icon = "face-sad-cry"
                case "2":
                    mood_icon = "face-sad-tear"
                case "3":
                    mood_icon = "face-meh"
                case "4":
                    mood_icon = "face-smile"
                case "5":
                    mood_icon = "face-grin-beam"

        days.append({
            'number': day,
            'note': daily_note,
            'classes': " ".join(classes),
            'mood': mood_icon,
        })

    years = []
    months = []

    earliest_year = Note.objects.filter(
        user=request.user,
    ).order_by("date").first().date.year

    current_year = timezone.now().year
    current_month = timezone.now().month

    for _year in range(earliest_year, current_year + 1):
        years.append(_year)

    if year == current_year:
        for _month in range(1, current_month + 1):
            months.append(MONTHS[_month - 1])
    else:
        month = MONTHS.copy()

    return render(request, 'notes/archive.html', {
        'days': days,
        'year': year,
        'month': month,
        'months': months,
        'years': years,
    })


def seek(request, year: int, month: int, day: int):
    note = get_object_or_404(
        Note,
        date__year=year,
        date__month=month,
        date__day=day
    )
    return render(request, 'notes/readonly.html', {
        "note": note,
    })
