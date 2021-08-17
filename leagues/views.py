from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"todas_ligas": League.objects.all(),
		"mujeres_ligas": League.objects.filter(name__contains = "Womens'"),
		"hockey_ligas": League.objects.filter(sport__contains = "hockey"),
		"no_football": League.objects.exclude(sport__contains = "football"),
		"conferencia_ligas": League.objects.filter(name__contains = "Conference"),
		"atlantica_ligas": League.objects.filter(name__contains = "Atlantic"),
		"dallas_team": Team.objects.filter(location = "Dallas"),
		"raptors_team": Team.objects.filter(team_name__contains = "Raptors"),
		"city_team": Team.objects.filter(location__contains = "City"),
		"t_team": Team.objects.filter(team_name__startswith = "T"),
		"order_team": Team.objects.all().order_by('location'),
		"inverso_team": Team.objects.all().order_by('-team_name'),
		"cooper_player": Player.objects.filter(last_name = "Cooper"),
		"joshua_player": Player.objects.filter(first_name = "Joshua"),
		"notjoshua_player": Player.objects.filter(last_name = "Cooper").exclude(first_name = "Joshua"),
		"two_player": Player.objects.filter(first_name = "Alexander") | Player.objects.filter(first_name = "Wyatt"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")