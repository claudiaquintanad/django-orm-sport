from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

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

def index2(request):
	context = {
		"equipos_atrantic": Team.objects.filter(league__name="Atlantic Soccer Conference"),
		"curr_boston": Player.objects.filter(curr_team__team_name = "Penguins", curr_team__location="Boston"),
		"curr_baseball": Player.objects.filter(curr_team__league__name = "International Collegiate Baseball Conference"),
		"lopez_player": Player.objects.filter(curr_team__league__name = "American Conference of Amateur Football", last_name= "Lopez"),
		"football_player": Player.objects.filter(curr_team__league__sport = "Football"),
		"team_sophia": Team.objects.filter(curr_players__first_name = "Sophia"),
		"ligas_sophia": League.objects.filter(teams__curr_players__first_name = "Sophia"),
		"player_flores": Player.objects.filter(last_name = "Flores").exclude(curr_team__team_name = "Roughriders", curr_team__location = "Washington"),
		"team_evans": Team.objects.filter(all_players__first_name = "Samuel", all_players__last_name = "Evans"),
		"team_cats": Player.objects.filter(all_teams__team_name = "Tiger-Cats", all_teams__location="Manitoba"),
		"wichita_player": Player.objects.filter(all_teams__team_name__contains = "Vikings", all_teams__location = "Wichita").exclude(curr_team__team_name = "Vikings", all_teams__location = "Wichita"),
		"jacob_team": Team.objects.filter(all_players__first_name = "Jacob", all_players__last_name = "Gray").exclude(team_name= "Colts", location="Oregon"),
		"joshua_player": Player.objects.filter(first_name = "Joshua", all_teams__league__name = "Atlantic Federation of Amateur Baseball Players"),
		"12_player": Team.objects.annotate(numero_jugadores = Count('all_players')).filter(numero_jugadores__gte = 12),
		"every_team": Player.objects.annotate(num_teams=Count("all_teams")).order_by("num_teams"),
	}
	return render(request, "index2.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")