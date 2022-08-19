from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect

from helloapp.utils import send_mail_to_user

# Create your views here.
# def hello_response(request):
#     return HttpResponse('Hello World!! from Django')

# def greetme(request,name):
#     return HttpResponse("Hello, {},How Are You?".format(name))

# def square(request,number):

#     sqr = number*number
#     return HttpResponse('Square is {}'.format(sqr))

# def multiply(request):
#     num1 = request.GET.get('num1')
#     num2 = request.GET.get('num2')
#     if num1 and num2:
#         result = int(num1)*int(num2)
#         return HttpResponse('Result is {}'.format(result))
#     else:
#         return HttpResponse('No params passed')
    

#       # print(request.GET)
#     # print(request.GET.get('num1'))
# def test(request):


#     return redirect('helloapp:hello_response')

# def send_mail(request):
#     message = request.GET.get('message')

#     send_mail_to_user(['test@gmail.com'],'Mail from Django',"THis is mail from django app and message is {}".format(message))
#     return HttpResponse("Mail sent to test@gmail.com ")

def index(request):
    return render(request,'base.html',{})

def helloapp(request):
    return render(request,'helloapp/helloapp.html',{})