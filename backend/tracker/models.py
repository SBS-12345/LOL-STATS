from django.db import models

class Summoner(models.Model):
    puuid = models.CharField(unique=True, max_length=100)
    riot_id = models.CharField(max_length=100)
    region = models.CharField(max_length=10)
    last_updated = models.DateTimeField(auto_now=True)

class Match(models.Model):
    match_id = models.CharField(max_length=50, unique=True)
    summoner = models.ForeignKey(Summoner, on_delete=models.CASCADE)
    champion = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    win = models.BooleanField()
    vision_score = models.IntegerField()
    gold_earned = models.IntegerField()
    damage_dealt = models.IntegerField()
    game_duration = models.IntegerField()
    game_date = models.DateTimeField()
