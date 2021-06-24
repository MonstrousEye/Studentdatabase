from django.shortcuts import render
from django.contrib import messages
from .models import Form
from django.http import HttpResponse
from django.views.generic import View



# Create your views here.
def base(request):

    return render(request,'base.html')

def form(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        branch=request.POST.get('branch')
        sem=request.POST.get('sem')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        college=request.POST.get('college')
        city=request.POST.get('city')
        state=request.POST.get('state')
        if len(fname)<1 or len(email)<3 or len(phone)<10 :
            messages.error(request,"please fill the valid details")
        
        else:
            form=Form(fname=fname,lname=lname,branch=branch,sem=sem,phone=phone,email=email,college=college,city=city,state=state)
            form.save()
            messages.success(request,"Your details has been recorded")
    return render(request,'form.html')



def student(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please Login and Come Again")
        return render(request,'index.html')
    else:
        allPosts=Form.objects.all()
        context={'allPosts': allPosts}
    return render(request,'student.html',context)


def search(request):
    query=request.GET['search']
    if len(query) == 0:
        allPosts=Form.objects.none()
    else:
        allPostsSno=Form.objects.filter(sno__icontains=query)
        allPosts=allPostsSno

    if allPosts.count() == 0:
        messages.warning(request,"No search Results")

    params={'allPosts':allPosts,'query':query}
    return render(request, 'search.html',params)



#Creating our view, it is a class based view
