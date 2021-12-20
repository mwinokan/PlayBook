
from .mdot import MDot

'''

To-Do's:

	Player: 
		- undo function animations
		- trail for cutting

'''

from copy import deepcopy

class Player(MDot):

	def __init__(self,**kwargs):
		super(Player,self).__init__(**kwargs)
		pass

	def undo(self):
		self.object.move_to(self._previous_position)

	def cut_to(self,target,trail=False):
		# trail: https://docs.manim.community/en/stable/reference/manim.animation.movement.MoveAlongPath.html
		self._previous_position = self.object.get_arc_center()
		return self.object.animate.move_to(target)
