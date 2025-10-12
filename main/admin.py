from django.contrib import admin
from .models import  *
from transfer.models import *

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', "president", 'coach', 'found_date', "country",)
    search_fields = ('name',)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'club', 'position', 'number', 'nation', 'age', 'price', )
    search_fields = ('name',)
    list_filter=('club', "nation", 'position', )
    ordering = ('number', 'age', 'price', )

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display =('player', 'old_club', 'new_club',  'price', 'price_tft', 'date', 'season', )
    search_fields = ('player', )
# Register your models here.
