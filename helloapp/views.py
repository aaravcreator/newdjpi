from django.shortcuts import render,HttpResponse

# Create your views here.
def hello_response(request):
    return HttpResponse('Hello World!! from Django')

def greetme(request,name):
    return HttpResponse("Hello, {},How Are You?".format(name))

def square(request,number):

    sqr = number*number
    return HttpResponse('Square is {}'.format(sqr))

def multiply(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    if num1 and num2:
        result = int(num1)*int(num2)
        return HttpResponse('Result is {}'.format(result))
    else:
        return HttpResponse('No params passed')
    

      # print(request.GET)
    # print(request.GET.get('num1'))