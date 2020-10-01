from django.shortcuts import render, get_object_or_404
from .models import Blog
def allblogs(request):
    blogs=Blog.objects.all().order_by('-pub_date')
    return render(request,'blogs/allblogs.html',{'blogs':blogs})


def detail(request,blog_id):
    detailblogs=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blogs/detail.html',{'blog':detailblogs})
