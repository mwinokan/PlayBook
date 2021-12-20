
from manim import *

from playbook import Player, Field, Squad, Disc, MScene, Pentagon

# config.background_color = GREEN

from copy import deepcopy

# manim -pql pentagon_intro.py PentagonIntro

class PentagonIntro(Scene):

	def construct(self):

		title = Tex("Pentagon",".",font_size=128)
		title.set_color(WHITE)
		
		pentagon = RegularPolygon(n=5,stroke_color=WHITE)
		pentagon.set_fill(WHITE,opacity=1.0)
		pentagon.rotate(-18*PI/180)
		pentagon.scale_to_fit_height(4)

		field = Field(scale=0.12,bricks=False)

		squad = Squad(fill=RED)
		squad.setup_pentagon(pentagon)
		player_handler1 = squad.objects[1]
		player_wing1 = squad.objects[0]
		player_handler2 = squad.objects[2]
		player_wing2 = squad.objects[3]
		player_deep = squad.objects[-1]

		disc = Disc()
		disc.object.next_to(player_handler1,UR,buff=0.1)

		# intro
		self.play(Write(title))
		self.play(*field.FadeIn())
		self.play(ReplacementTransform(title,pentagon))
		self.play(*squad.Create(), Create(disc.object), FadeOut(pentagon))

		#####
		
		# deep -> central
		self.play(player_deep.animate.shift(LEFT*2))
		self.play(disc.object.animate.next_to(player_deep,LEFT,buff=0.1))
		self.play(disc.object.animate.next_to(player_deep,RIGHT,buff=0.1))

		# handler -> deep
		self.play(player_handler2.animate.shift(UP+RIGHT*4))
		self.play(disc.object.animate.next_to(player_handler2,UP,buff=0.1))

		# shift up pentagon
		self.play(
			player_wing1.animate.shift(RIGHT*2),
			player_wing2.animate.shift(RIGHT*2),
			player_handler1.animate.shift(RIGHT*2)
		)

		self.wait()

class PentagonExplainer(Scene):

	def construct(self):
		
		### title

		title = Tex("Pentagon",".",font_size=128)
		title.set_color(WHITE)

		field = Field(scale=0.12,bricks=False)
		self.field = field

		self.play(Write(title))
		self.play(*field.FadeIn())

		### concept

		concept_text1 = Tex("Pentagon",font_size=32)
		concept_text2 = Tex(" is an unpredictable offence",font_size=32)
		concept_text3 = Tex("that allows for creative cutting and throwing.",font_size=32)

		concept_text1.next_to(field._endzone1,buff=0.5)
		concept_text1.shift(UP*0.3)
		concept_text2.next_to(concept_text1,RIGHT,buff=0.1)
		concept_text3.next_to(field._endzone1,buff=0.5)
		concept_text3.shift(DOWN*0.3)

		self.play(TransformMatchingTex(title,concept_text1))
		self.play(Write(concept_text2))
		self.play(Write(concept_text3))

		self.play(
			FadeOut(concept_text1),
			FadeOut(concept_text2),
			FadeOut(concept_text3),
			)

		### formation

		pentagon = RegularPolygon(n=5,stroke_color=WHITE)
		pentagon.set_fill(WHITE,opacity=1.0)
		pentagon.rotate(-18*PI/180)
		pentagon.scale_to_fit_height(4)

		self.top_text("Players set up in a pentagonal formation.")			
		
		self.play(Create(pentagon))

		squad = Squad(fill=RED)
		squad.setup_pentagon(pentagon)
		player_handler1 = squad.objects[1]
		player_wing1 = squad.objects[0]
		player_handler2 = squad.objects[2]
		player_wing2 = squad.objects[3]
		player_deep = squad.objects[-1]

		disc = Disc()
		disc.object.next_to(player_handler1,UR,buff=0.1)

		self.play(*squad.Create(), Create(disc.object), FadeOut(pentagon))

		self.clear_last_text()

		self.top_text("Any of the players can attack the large open space.")

		for p in [player_wing1,player_deep,player_wing2,player_handler2]:
			p_old = deepcopy(p)
			self.play(p.animate.next_to(squad.center,RIGHT,buff=0.0))
			p.next_to(p_old,RIGHT,buff=0.0)
		
		self.clear_last_text()

		### throw

		self.top_text("If the cutter is free, they should be thrown to.")

		self.play(player_wing2.animate.next_to(squad.center,RIGHT,buff=0.0))
		self.play(disc.object.animate.next_to(player_wing2,UR,buff=0.1))

		self.clear_last_text()

		### continuation throw

		self.top_text("If there is a free pass forward, take it.")

		self.play(disc.object.animate.next_to(player_deep,RIGHT,buff=0.1))
		disc.object.next_to(squad.center,UR,buff=0.1)
		self.play(disc.object.animate.next_to(player_wing1,DR,buff=0.1))
		disc.object.next_to(squad.center,UR,buff=0.1)

		# self.clear_last_text()
		# self.top_text("There are usually several options")

		self.clear_last_text()
		
		### continuation cuts
		
		self.top_text("Continuation cuts are also effective")

		target = squad.wing2(new=True)
		start_disc = deepcopy(disc).object
		for p in [player_handler1,player_deep]:
			start_p = deepcopy(p)
			self.play(disc.object.animate.next_to(target,RIGHT,buff=0.1),
					  p.animate.next_to(target,RIGHT,buff=0.0))
			disc.object.move_to(start_disc)
			p.move_to(start_p)

		self.play(disc.object.animate.next_to(target,RIGHT,buff=0.1),
				  player_handler2.animate.next_to(target,RIGHT,buff=0.0))

		self.clear_last_text()

		self.wait()

		### continuation throws
		
		self.top_text("Once the disc settles. Re-form the pentagon.")

		self.play(
		player_handler1.animate.shift(RIGHT*2.2),
		player_wing1.animate.shift(RIGHT*2.2),
		player_wing2.animate.shift(RIGHT*2.2+DOWN*1.8),
		player_deep.animate.shift(RIGHT*2.2)
		)

		# handler1 -> handler1
		# wing1 -> wing1
		# handler2 -> handler2
		# deep -> deep

	def top_text(self,text,font_size=32,create=True):

		text = Tex(text)
		text.next_to(self.field._central,UP,buff=0.5)

		if create:
			self.play(Write(text))

		self._last_text = text

		return text

	def clear_last_text(self):
		self.remove(self._last_text)

class PentagonClassTest(MScene):

	def construct(self):

		# create a title
		self.title("Pentagon.",subtext="by Max Winokan")

		# any manim animation method can be passed
		self.create_field(method=FadeIn)

		# clear the text
		self.clear_last_text(FadeOut)

		# set up the offence
		self.offence = Pentagon()

		### TODO
		# show the offence
		self.play(self.offence.shape_method(Create))

		### TODO
		# fade out the offence and hide the shape
		self.play(
					self.offence.FadeOutShape(),
					*self.offence.Create(),
				 )

		### TODO
		# try making a cut
		# self.play(self.offence.deep().animate.move_to(self.offence.center))
		# self.play(self.offence.deep().cut_to(self.offence.center))
		self.new_cut(self.offence.deep(),self.offence.center)

		# undo the cut
		self.offence.deep().undo()

		# move the offence
		

		# wait (and process any queued actions)
		self.wait()