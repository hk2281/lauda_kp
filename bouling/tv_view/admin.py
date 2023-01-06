from django.contrib import admin
from .models import Players, Command, Ligue, Game, ClubMeta
# Register your models here.


class a_players(admin.ModelAdmin):
    list_display = [
        'player','comand_id','first_name','last_name','contact_info','way','throw_count','avarege_score',]

class a_command(admin.ModelAdmin):
    list_display = ['command','comand_name','score',]

class a_club(admin.ModelAdmin):
    list_display = ['club','club_name','address','way_count',]

class a_ligue(admin.ModelAdmin):
    list_display = ['ligue','ligue_name','club_id',]
class a_game(admin.ModelAdmin):
    list_display = ['game','game_name','game_date',]

admin.site.register(Players,a_players)
admin.site.register(Command,a_command)
admin.site.register(Game,a_game)
admin.site.register(Ligue,a_ligue)
admin.site.register(ClubMeta,a_club)
