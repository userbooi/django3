from django.shortcuts import render

# Create your views here.
def home(request):
    info = {'message':"hi, I like to code with python and html, it is one of my hobbies"}
    return render(request, 'index.html', info)