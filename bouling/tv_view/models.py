

from django.db import models
from django.conf import settings

# Create your models here.

class ClubMeta(models.Model):

    club = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=30, default=None, unique=True)
    address = models.CharField(max_length=30)
    way_count = models.IntegerField()

    def __str__(self) -> str:
        return self.club_name

class Ligue(models.Model):
    ligue = models.AutoField(primary_key=True)
    ligue_name = models.CharField(max_length=30)
    club_id = models.ForeignKey(ClubMeta, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ligue_name


class Game(models.Model):
    game = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=30)
    game_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.game_name
    

class Command(models.Model):
    command = models.AutoField(primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, default=None)
    lugue_id = models.ForeignKey(Ligue, on_delete=models.CASCADE, default=None)
    comand_name = models.CharField(max_length=50)
    score = models.FloatField()

    def __str__(self) -> str:
        return self.comand_name
    


class Players(models.Model):
    """this class describe player entity model"""
    player = models.AutoField(primary_key=True)
    comand_id = models.ForeignKey(Command, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_info = models.CharField(max_length=30)
    way = models.IntegerField()
    throw_count = models.IntegerField()
    avarege_score = models.FloatField()

    def __str__(self) -> str:
        return self.last_name




