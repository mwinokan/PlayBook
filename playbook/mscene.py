
from .field import Field

from manim import *

'''

To-Do's:

	- Test field adding/removal
	- Deal with offence animation better

'''

class MScene(Scene):

	def __init__(self):
		config.background_color = GREEN
		super(MScene, self).__init__()

	def title(self, text, subtext=None, create=True, size=128, subsize=32, delay_sub=True):

		text = Tex(text,font_size=size)

		if subtext is not None:
			subtext = Tex(subtext,font_size=subsize)
			subtext.next_to(text,DOWN,buff=0.5)
			self._last_text = [text,subtext]
			if create:
				if delay_sub:
					self.play(Write(text))
					self.play(Write(subtext))
				else:
					self.play(Write(text),Write(subtext))
			return [text,subtext]
		
		if create:
			self.play(Write(text))

		self._last_text = text
		return text
		
	def top_text(self,text,font_size=32,create=True):

		text = Tex(text)
		text.next_to(self.field._central,UP,buff=0.5)

		if create:
			self.play(Write(text))

		self._last_text = text

		return text

	def create_field(self,method=None):
		self._field = Field(scale=0.12,bricks=False)
		if method is not None:
			self.play(*self._field.method(method))
		return self._field

	def add_field(self,method=None):
		self.add(*self.field.objects)
		return self.field

	def remove_field(self,method=None):
		self.remove(*self.field.objects)

	def clear_last_text(self):
		if isinstance(self._last_text,list):
			for t in self._last_text:
				self.remove(t)
		else:
			self.remove(self._last_text)

	@property
	def field(self):
		if self._field is not None:
			return self._field
		else:
			return self.create_field()
	