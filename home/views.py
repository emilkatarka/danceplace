from django.shortcuts import render


app_name = 'home' #namespace

def home(request):
    return render(request, 'home/home.html')


