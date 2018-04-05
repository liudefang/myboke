# Create your views here.
from django.contrib.auth import authenticate,login    #①
from django.http import HttpResponse
from django.shortcuts import render
from account.forms import LoginForm


def user_login(request):  #②
    if request.method == "POST":     #③
        login_form = LoginForm(request.POST)    #④
        if login_form.is_valid():    #⑤
            cd = login_form.cleaned_data    #⑥
            user = authenticate(username=cd['username'],password=cd['password'])    #⑦
            if user:
                login(request,user) #⑧
                return HttpResponse("wellcome you.you have been authenticated successfully")  #⑨
            else:
                return HttpResponse("Sorry You username or password is not right.")
        else:
            return HttpResponse("Ivalid login")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request,"account/login.html",{"form":login_form})

