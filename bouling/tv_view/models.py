

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class ClubMeta(models.Model):

    club = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=30, default=None, unique=True,blank=False)
    address = models.CharField(max_length=30, blank=False)
    way_count = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return self.club_name

class Ligue(models.Model):
    ligue = models.AutoField(primary_key=True)
    ligue_name = models.CharField(max_length=30, blank=False)
    club_id = models.ForeignKey(ClubMeta, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.ligue_name


class Game(models.Model):
    game = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=30,blank=False)
    game_date = models.DateTimeField(blank=True)

    def __str__(self) -> str:
        return self.game_name
    

class Command(models.Model):
    command = models.AutoField(primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, default=None)
    lugue_id = models.ForeignKey(Ligue, on_delete=models.CASCADE, default=None)
    comand_name = models.CharField(max_length=50, blank=False)
    score = models.FloatField(blank=True)

    def __str__(self) -> str:
        return self.comand_name
    


class Players(models.Model):
    """this class describe player entity model"""
    player = models.AutoField(primary_key=True)
    comand_id = models.ForeignKey(Command, on_delete = models.CASCADE, default=None)
    first_name = models.CharField(max_length=30,blank=False)
    last_name = models.CharField(max_length=30,blank=False)
    contact_info = models.CharField(max_length=30,blank=True)
    way = models.IntegerField(blank=True,validators=[MinValueValidator(0),
                                  MaxValueValidator(100)])
    throw_count = models.IntegerField(blank=True, validators=[MinValueValidator(0),
                                  MaxValueValidator(100)])
    avarege_score = models.FloatField()

    def __str__(self) -> str:
        return self.last_name




