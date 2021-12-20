
from manim import *

class Field():

	def __init__(self,fill=None,stroke=WHITE,opacity=1.0,strokeWidth=4,scale=0.1,bricks=False):

		self._fill = fill
		self._stroke = stroke
		self._opacity = opacity
		self._strokeWidth = strokeWidth
		self._scale = scale
		self._bricks = bricks

		self.make()
	
	def make(self):

		self._central = Rectangle(height=37*self._scale,width=64*self._scale)
		self._endzone1 = Rectangle(height=37*self._scale,width=18*self._scale)
		self._endzone2 = Rectangle(height=37*self._scale,width=18*self._scale)

		self._brick1 = Cross(stroke_color=self._stroke,stroke_width=self._strokeWidth,scale_factor=self._scale)
		self._brick2 = Cross(stroke_color=self._stroke,stroke_width=self._strokeWidth,scale_factor=self._scale)

		for o in self.objects:
			if self._fill is not None:
				o.set_fill(self._fill,opacity=self._opacity)
			else:
				o.set_fill(self._fill,opacity=0.0)

			o.set_stroke(self._stroke,opacity=self._opacity,width=self._strokeWidth)

		self._endzone1.next_to(self._central, LEFT, buff=0)
		self._endzone2.next_to(self._central, RIGHT, buff=0)

		self._brick1.next_to(self._endzone1, RIGHT, buff=self._scale*18)
		self._brick2.next_to(self._endzone2, LEFT, buff=self._scale*18)
		
	@property
	def objects(self):
		if self._bricks:
			return [self._central, self._endzone1, self._endzone2, self._brick1, self._brick2]
		else:
			return [self._central, self._endzone1, self._endzone2]

	def method(self,method):
		return tuple([method(o) for o in self.objects])

	def Create(self):
		return self.method(Create)

	def FadeIn(self):
		return self.method(FadeIn)
