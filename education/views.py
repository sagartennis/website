from django.shortcuts import render
from .models import Education
# Create your views here.
def education(request):
    edu = Education.objects
    return render(request,'education.html',{'edu':edu})
