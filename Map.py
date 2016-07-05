class Map(object):

	scenes = {
		'main_room': MainRoom(),
		'first_offense': FirstOffense(),
		'ranged_path': RangedPath() ,
		'agree': Agree(),
		'disagree': Disagree(),
		'finished': Finished(),
		'death': Death()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)