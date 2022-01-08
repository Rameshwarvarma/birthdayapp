from django.shortcuts import render, redirect
from bdaywishapp.forms import BirthdayForm
from .models import Birthday
from datetime import date


# Create your views here.


def index(request):
    birthdays = []
    for dt in Birthday.objects.all():
        if dt.isBirthdayToday():
            birthdays.append(dt)

    context = {'birthdays': birthdays}
    return render(request, 'index.html', context)


def details(request):
    if request.method == 'POST':
        form = BirthdayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')

    else:
        form = BirthdayForm()

    return render(request, 'enter.html', {'form': form})


def show(request):
    birthday = Birthday.objects.all()
    return render(request, 'show.html', {'birthday': birthday})
