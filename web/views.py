from django.shortcuts import render

from web.models import Student

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})



def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Sveikiname! Jūsų paskyra sukurta sėkmingai!")
    else:
        form = UserCreationForm()
        return render(request, 'auth/create_user.html', {'form': form})