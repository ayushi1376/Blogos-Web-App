from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post

# Create your views here.def home(index):
def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        print(name,email,phone,content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<10:
            messages.error(request,"Please fill the form correctlt!")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"Your response has been submitted.")

    return render(request,'home/contact.html')

def search(request):
    query=request.GET['query']
    # allPosts=Post.objects.all()
    allPosts=Post.objects.filter(title__icontains=query)
    params={'allPosts':allPosts}
    return render(request,'home/search.html',params)
    # return HttpResponse('This is search')
