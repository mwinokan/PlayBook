
from manim import *

from .player import Player

'''

To-Do's:

	- shift entire squad?

'''

class Squad():

	def __init__(self,size=5,fill=WHITE,stroke=WHITE,opacity=1.0,strokeWidth=1):

		self._fill = fill
		self._stroke = stroke
		self._opacity = opacity
		self._strokeWidth = strokeWidth

		self._players = []
		for i in range(size):
			self._players.append(self.make_player())

	def make_player(self,object=False):
		p = Player(fill=self._fill,
					  stroke=self._stroke,
					  opacity=self._opacity,
					  strokeWidth=self._strokeWidth)

		if object:
			return p.object
		else: 
			return p

	@property
	def group(self):
		return VGroup(*self.objects)

	@property
	def objects(self):
		return [p.object for p in self.players]

	@property
	def players(self):
		return self._players

	def get_player(self,index,new,object):
		print(self.objects)
		print(self.players)
		if new:
			return self.make_player(object=object).move_to(self.shape.get_vertices()[index])
		if object:
			return self.objects[index]
		else:
			return self.players[index]

	def method(self,method):
		return tuple([method(o) for o in self.objects])

	def Create(self):
		return self.method(Create)

	def FadeIn(self):
		return self.method(FadeIn)
