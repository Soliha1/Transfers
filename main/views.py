from django.forms import FloatField
from django.shortcuts import render, get_object_or_404
from django.db.models import F, ExpressionWrapper, Func
from transfer.models import Season
from .models import *
from transfer.models import *

def home_view(request):
    return render(request, 'index.html')


def clubs_view(request):
    clubs=Club.objects.all()

    country_query=request.GET.get('country')
    if country_query:
        clubs=clubs.filter(country__id=country_query)
    context={
        'clubs':clubs
    }
    return render(request, 'clubs.html', context)

def latest_transfers_view(request):
    latest=Season.objects.last()
    transfers=Transfer.objects.filter(season=latest).order_by('-price')
    context={
        'latest':latest,
        'transfers':transfers,
    }
    return render(request, 'latest-transfers.html', context)

def U_20_players_view(request):
    players=Player.objects.filter(age__lte=20)
    context={
        'players':players,
    }
    return render(request, 'U-20 players.html', context)

def Players_view(request):
    players=Player.objects.all()
    context={
        'players':players,
    }
    return render(request, 'players.html', context)


def Tryouts_view(request):
    return render(request, 'tryouts.html')

def About_view(request):
    return render(request, 'about.html')

def club_retrive_view(request, pk):
    club=get_object_or_404(Club, pk=pk)
    players=Player.objects.filter(club=club).order_by('-price')
    context={
        'club':club,
        'players':players,
    }
    return render(request, 'club-info.html', context)


def Stats_view(request):
    return render(request, 'stats.html')


def stats_top_150_accurate_predictions(request):
    transfers = Transfer.objects.annotate(
        accurate_predictions=ExpressionWrapper(
            Func(
                F('price') - F('price_tft') / F('price_tft') * 100,
                function='ABS'
            ),
            output_field=FloatField()
        )
    ).order_by('accurate_predictions')
    context={
        'transfers':transfers,
    }
    return render(request,'stats/150-accurate-predictions.html')


def top_50_clubs_by_expenditure_view(request):
    transfers = Transfer.objects.all().order_by('price')[:50]
    context={
        'transfers':transfers,
    }

    return render(request, 'stats/top-50-clubs-by-expenditure-in-2021.html', context)

def top_50_clubs_by_income_view(request):
    transfers = Transfer.objects.all().order_by('-price')[:50]
    context={
        'transfers':transfers,
    }
    return render(request, 'stats/top-50-clubs-by-income-in-2021.html', context)

def transfer_records_view(request):
    transfers=Transfer.objects.all()
    context={
        'transfers':transfers
    }
    return render(request, 'stats/transfer-records.html', context)