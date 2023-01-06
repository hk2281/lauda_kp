

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
# Create your models here.

class ClubMeta(models.Model):

    club = models.AutoField(primary_key=True,verbose_name='id клуба')
    club_name = models.CharField(max_length=30, default=None, unique=True,verbose_name='название')
    address = models.CharField(max_length=30,verbose_name='адрес')
    way_count = models.IntegerField(validators=[MinValueValidator(0)],verbose_name='кол-во дорожек')

    def __str__(self) -> str:
        return self.club_name

    class Meta:
        verbose_name = _('данные клуба')
        verbose_name_plural = _('данные клубов')

class Ligue(models.Model):
    ligue = models.AutoField(primary_key=True,verbose_name='id лиги')
    ligue_name = models.CharField(max_length=30,verbose_name='название лиги')
    club_id = models.ForeignKey(ClubMeta, on_delete=models.CASCADE,verbose_name='клуб')

    def __str__(self) -> str:
        return self.ligue_name

    class Meta:
       verbose_name = _('лига')
       verbose_name_plural = _('лиги')


class Game(models.Model):
    game = models.AutoField(primary_key=True,verbose_name='id игры')
    game_name = models.CharField(max_length=30,verbose_name='название игры')
    game_date = models.DateTimeField(verbose_name='дата проведения')

    def __str__(self) -> str:
        return self.game_name

    class Meta:
       verbose_name = _('игра')
       verbose_name_plural = _('игры')
    

class Command(models.Model):
    command = models.AutoField(primary_key=True,verbose_name='id команды')
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, default=None,verbose_name='учавствует в игре')
    lugue_id = models.ForeignKey(Ligue, on_delete=models.CASCADE, default=None,verbose_name='принадлежит лиге')
    comand_name = models.CharField(max_length=50,verbose_name='название команды')
    score = models.FloatField(validators=[MinValueValidator(0.0)],verbose_name='баллы')

    def __str__(self) -> str:
        return self.comand_name

    class Meta:
       verbose_name = _('команда') 
       verbose_name_plural = _('команды')  


class Players(models.Model):
    """this class describe player entity model"""
    player = models.AutoField(primary_key=True,verbose_name='id игрока')
    comand_id = models.ForeignKey(Command, on_delete = models.CASCADE,verbose_name='член команды')
    first_name = models.CharField(max_length=30,verbose_name='имя')
    last_name = models.CharField(max_length=30,verbose_name='фамилия')
    contact_info = models.CharField(max_length=30,verbose_name='контактная информация')
    way = models.IntegerField(validators=[MinValueValidator(1)],verbose_name='дорожка')
    throw_count = models.IntegerField(validators=[MinValueValidator(0)],verbose_name='кол-во бросков')
    avarege_score = models.FloatField(validators=[MinValueValidator(0.0)],verbose_name='среднее кол-во баллов')

    def __str__(self) -> str:
        return self.last_name

    class Meta:
       verbose_name = _('игрок')
       verbose_name_plural = _('игроки')


