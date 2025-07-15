from django.contrib import admin
from .models import Game

# Optional: customize admin display
class GameAdmin(admin.ModelAdmin):
    list_display = ("id", "player_x", "player_o", "winner")  # Adjust fields as in your Game model

admin.site.register(Game, GameAdmin)