
from .squad import Squad

from manim import *

'''

To-Do's

	- update polygon to current positions

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

		for point,player in zip(vertices,self.players):
			player.object.move_to(point)

	def handler1(self,new=False,object=False):
		return self.get_player(1,new=new,object=object)

	def handler2(self,new=False,object=False):
		return self.get_player(2,new=new,object=object)

	def wing1(self,new=False,object=False):
		return self.get_player(0,new=new,object=object)

	def wing2(self,new=False,object=False):
		return self.get_player(3,new=new,object=object)

	def deep(self,new=False,object=False):
		return self.get_player(4,new=new,object=object)

	def shape_method(self,method):
		return method(self._polygon)

	def CreateShape(self):
		return self.shape_method(Create)

	def FadeInShape(self):
		return self.shape_method(FadeIn)

	def FadeOutShape(self):
		return self.shape_method(FadeOut)

	def shift(self,direction):
		self.shape.shift(direction)
		for p in self.objects:
			p.shift(direction)

	@property
	def center(self):
		vertices = self.shape.get_vertices()
		x = sum(v[0] for v in vertices)/len(vertices)
		y = sum(v[1] for v in vertices)/len(vertices)
		return [x,y,0]
		# d = Dot()
		# d.move_to([x,y,0])
		# return d

	@property
	def shape(self):
		return self._polygon
	