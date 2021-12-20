
from manim import *

class MDot():

	def __init__(self,fill=WHITE,stroke=WHITE,opacity=1.0,strokeWidth=1):
		
		self._fill = fill
		self._stroke = stroke
		self._opacity = opacity
		self._strokeWidth = strokeWidth

		self.make()

	def make(self):
		self._object = Dot()
		self._object.set_fill(self._fill,opacity=self._opacity)
		self._object.set_stroke(self._stroke,opacity=self._opacity)

	@property
	def object(self):
		# print(type(self))
		return self._object
