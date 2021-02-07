from django.shortcuts import render

# Create your views here.
def home(request):
    info = {'key':"value of key"}
    return render(request, 'anything.html', info)