from django.shortcuts import render

# Create your views here.
def tennis(request):
    return render(request,'tennis.html')
