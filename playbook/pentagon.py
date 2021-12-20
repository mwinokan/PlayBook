
from .squad import Squad

from manim import *

'''

To-Do's

	- correct center
	- shift functionality

'''

class Pentagon(Squad):
	"""docstring for Pentagon"""
	def __init__(self,polygon=None):
		super(Pentagon, self).__init__()

		if polygon is not None:
			self.setup_pentagon(polygon)
		else:
			# setup the default shape
			pentagon = RegularPolygon(n=5,stroke_color=WHITE)
			pentagon.set_fill(WHITE,opacity=1.0)
			pentagon.rotate(-18*PI/180)
			pentagon.scale_to_fit_height(4)
			self.setup_pentagon(pentagon)

	# def create_shape(self):

	def setup_pentagon(self,polygon):

		self._polygon = polygon

		vertices = polygon.get_vertices()

		# self._players = []
		# for vertex in vertices:
		# 	self._players.append(Player(fill=self._fill,stroke=self._stroke,opacity=self._opacity,strokeWidth=self._strokeWidth))

		for point,player in zip(vertices,self.players):
			player.object.move_to(point)

	def handler1(self,new=False):
		if new:
			return self.make_player(object=True).move_to(self._pentagon.get_vertices()[1])
		return self.objects[1]

	def handler2(self,new=False):
		if new:
			return self.make_player(object=True).move_to(self._pentagon.get_vertices()[2])
		return self.objects[2]

	def wing1(self,new=False):
		if new:
			return self.make_player(object=True).move_to(self._pentagon.get_vertices()[0])
		return self.objects[0]

	def wing2(self,new=False):
		if new:
			return self.make_player(object=True).move_to(self._pentagon.get_vertices()[3])
		return self.objects[3]

	def deep(self,new=False):
		if new:
			return self.make_player(object=True).move_to(self._pentagon.get_vertices()[4])
		return self.objects[4]

	def shape_method(self,method):
		return method(self._polygon)

	def CreateShape(self):
		return self.shape_method(Create)

	def FadeInShape(self):
		return self.shape_method(FadeIn)

	def FadeOutShape(self):
		return self.shape_method(FadeOut)

	@property
	def shape(self):
		return self._polygon
	