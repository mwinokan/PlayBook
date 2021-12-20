
from .mdot import MDot

'''

To-Do's:

	Player: 
		- cutting function
		- trail for cutting
		- undo function

'''

class Player(MDot):

	def __init__(self,**kwargs):
		super(Player,self).__init__(**kwargs)
		pass

	def cut_to(self,scene,point):
		if len(point) == 2:
			point = point + [0]
		return self.object.move_to(point).copy()
		# scene.play(ReplacementTransform(self.object,self.object.move_to(point)),run_time=3)
