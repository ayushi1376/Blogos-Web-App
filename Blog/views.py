from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,Blogcomment
from django.contrib import messages
from blog.templatetags import extras


# Create your views here.
def blogHome(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog/blogHome.html',context)
    

def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments=Blogcomment.objects.filter(post=post,parent=None)
    reply=Blogcomment.objects.filter(post=post).exclude(parent=None)
    repDict={}
    for r in reply:
        if r.parent.sno not in repDict.keys():
            repDict[r.parent.sno]=[r]
        else:
            repDict[r.parent.sno].append(r)
    context={'post':post,'comments':comments, 'user': request.user, 'repDict': repDict}
    return render(request,'blog/blogPost.html',context)
    

def postComment(request):
    if request.method=='POST':
        comment= request.POST.get("comment")
        user= request.user
        postSno=request.POST.get("postSno") 
        post=Post.objects.get(sno=postSno)
        parentSno=request.POST.get("parentSno")
        if parentSno=="":
            comment=Blogcomment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request, "Your comment has been successfully posted")
        else:
            parent=Blogcomment.objects.get(sno=parentSno)
            comment=Blogcomment(comment=comment,user=user,post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has posted")

    return redirect(f'/blog/{post.slug}')

    
    