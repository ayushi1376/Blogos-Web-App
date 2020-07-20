from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
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
            messages.error(request,"Please fill the form correctly!")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"Your response has been submitted.")

    return render(request,'home/contact.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle=Post.objects.filter(title__icontains=query)
        allPostsContent=Post.objects.filter(content__icontains=query)
        allPostsAuthor=Post.objects.filter(author__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request,"Sorry, no search results found. Please refine your query!")

    params={'allPosts':allPosts,'query':query}
    return render(request,'home/search.html',params)

def handleSignup(request):
    if request.method=='POST':
        # get the post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        #check for errorneous inputs
        if len(username) > 10:
            messages.error(request,"Username must be under 10 characters")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request,"Username must contain letters and numbers")
            return redirect('home')
        
        if pass1!=pass2:
            messages.error(request,"Passwords do not match")
            return redirect('home')
        
        #Create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your Blogger account has been successfully created.")
        return redirect('home')


    else:
        return HttpResponse('404-Not Found')