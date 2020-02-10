from django.db import models

class Note(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	
class Raid(models.Model):
	title = models.TextField()
	date = models.DateField()
	time = models.DateTimeField()
	instance = models.TextField()
	
class GameNight(models.Model):
	organizer = models.TextField()
	game_name = models.TextField()
	time = models.DateTimeField()

def __str__(self):
	return '%s %s' % (self.title, self.body)
