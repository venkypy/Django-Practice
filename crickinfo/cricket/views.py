from django.shortcuts import render
from django.http import HttpResponse


def matches_view(request):
    return render(request, 'cricket/matches.html')


def fun(request):
    # read the data from cricket/templates/players.html and create HttpResponse
    resp = render(request, 'cricket/players.html')
    return resp
