from django.shortcuts import render


def work(request):
    return render(request,'job.html')
