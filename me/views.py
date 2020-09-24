from django.shortcuts import render, get_object_or_404
from .models import Me
def about(request):
    me=Me.objects
    return render(request,'me/about.html',{'me':me})
