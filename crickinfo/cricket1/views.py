from django.shortcuts import render


def fun1(request):
    resp = render(request,'cricket1/players.html')
    return resp

