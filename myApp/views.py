from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


@login_required
def home(request):
    return render(request, 'myApp/home.html')


def signup(request):
    context = {}
    form = UserCreationForm(request.POST)
    print(f'{form=}')
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'myApp/home.html')
    context['form'] = form
    return render(request, 'registration/signup.html', context)
