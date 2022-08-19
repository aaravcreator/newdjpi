from django.shortcuts import render,HttpResponse

# Create your views here.
def hello_response(request):
    return HttpResponse('Hello World!! from Django')