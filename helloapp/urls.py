"""djproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from helloapp import views

app_name = "helloapp"

urlpatterns = [
#    path("",views.hello_response,name='hello_response'),
    path("",views.index,name='index'),
     path("hello/",views.helloapp,name='helloapp'),
#    path('greet/<str:name>',views.greetme,name='greetme'),
#    path('square/<int:number>',views.square,name='square'),
#    path('multiply/',views.multiply,name='multiply'),
#    path('test/',views.test,name='test'),
#    path('send_mail/',views.send_mail,name='send_mail'),
]
