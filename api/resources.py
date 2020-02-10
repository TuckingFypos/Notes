# api/resources.py

from tastypie.resources import ModelResource
from api.models import Note
from api.models import Raid
from api.models import GameNight
from tastypie.authorization import Authorization

class NoteResource(ModelResource):
	class Meta:
		queryset = Note.objects.all()
		resource_name = 'note'
		authorization = Authorization()

class RaidResource(ModelResource):
	class Meta:
		queryset = Raid.objects.all()
		resource_name = 'raid'
		authorization = Authorization()

class GameNightResource(ModelResource):
	class Meta:
		queryset = GameNight.objects.all()
		resource_name = 'game night'
		authorization = Authorization()
