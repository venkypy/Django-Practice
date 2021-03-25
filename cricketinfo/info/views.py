from django.shortcuts import render, redirect
from info.models import Country, Player, Player2
from info.forms import Player2Form

def home_view(request):
    return render(request, 'info/home.html')

def players2_view(request):
    player2 = Player2.objects.all()
    return render(request,'info/players2.html', {"player2":player2})

def create_player2_view(request):
    msg = ""
    if request.method == "POST":
        data = request.POST
        form = Player2Form(data=data)
        if form.is_valid():
            form.save()
            return redirect('/players2')
        else:
            msg = form._errors
    else:
        form = Player2Form()
    return render(request,'info/create_player2.html', {"form":form, "message":msg})


def countries_view(request):
    countries = Country.objects.all()
    return render(request, 'info/countries.html', {"countries":countries})

def add_country_view(request):
    msg=""
    if request.method == "POST":
        data = request.POST
        c = Country(name=data['name'],
                    shortname=data['shortname'],
                    description=data['description']
                    )
        try:
            c.save()
            msg="Country created successfully"
            return redirect('/countries',{"message":msg})
        except Exception as err:
            msg = err

    return render(request, 'info/add_country.html')

def update_country_view(request,pk):
    country = Country.objects.filter(id=pk)
    country = country[0]
    msg = ""
    if request.method == "POST":
        data = request.POST
        country.name = data['name']
        country.shortname = data['shortname']
        country.description = data['description']
        country.save()
        msg = "Country updated successfully"
        return redirect("/countries", {"message":msg})
    return render(request,'info/update_country.html', {"data":country})

def delete_country_view(request,pk):
    country = Country.objects.filter(id=pk)
    country = country[0]
    country.delete()
    return redirect('/countries')

def players_view(request):
    player = Player.objects.all()
    return render(request, 'info/players.html',{'player':player})

def add_player_view(request):
    msg = ""
    if request.method == "POST":
        data = request.POST
        p = Player(name=data['name'],
                   country=data['country'],
                   role=data['role'],
                   hs=data['hs']
                   )
        p.save()
        msg = "Player successfully added into the Player Table"
        return redirect('/players')
    return render(request,'info/add_player.html', {"message":msg})

def update_player_view(request,pk):
    player = Player.objects.get(id=pk)
    if request.method == "POST":
        data = request.POST
        player.name = data['name']
        player.country = data['country']
        player.role = data['role']
        player.hs = data['hs']
        player.save()
        return redirect('/players')
    return render(request,'info/update_player.html', {'player':player})

def delete_player_view(request,pk):
    player = Player.objects.get(id=pk)
    player.delete()
    return redirect('/players')
