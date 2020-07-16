from django.shortcuts import render,HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse('This is blogHome. we will keep all blog post here')
def blogPost(request,slug):
    return HttpResponse(f'This is blogPost:{slug}')