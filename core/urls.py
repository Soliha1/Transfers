"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('club/', clubs_view, name='club'),
    path('club/<int:pk>/', club_retrive_view, name='club-info'),
    path('latest_transfers/', latest_transfers_view, name='latest transfers'),
    path('players/', Players_view, name='Players'),
    path('U-20 players/', U_20_players_view, name='20 players'),
    path('tryouts/', Tryouts_view, name='tryouts'),
    path('about/', About_view, name='about'),
    path('stats/', Stats_view, name='stats'),
    path('stats/top-150-accurate-predictions/', stats_top_150_accurate_predictions, name='top-150'),
    path('stats/top-50-clubs-by-expenditure', top_50_clubs_by_expenditure_view, name='top-50'),
    path('stats/top-50-clubs-by-incomes', top_50_clubs_by_income_view, name='top-50 incomes'),
    path('stats/transfer_records', transfer_records_view, name='records')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)