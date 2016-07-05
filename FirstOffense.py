class FirstOffense(Scene):
	def enter(self):
		print "After the last zergling attack, one of your zealots has died."
		print "You have 3 left."
		print "You can build up your army now, but can only choose one type of unit."
		print "Do you want to train: "
		print "A. More void rays"
		print "B. More zealots"
		print "C. More stalkers"

		army = raw_input("> ")

		if army == "A":
			print "You choose the air path." 
			print "You sucessfully build up an army of void rays that are 6 in number."
			print "As you begin to send out your fleet, a terran marine shows up at the gates."
			print "He tells you Jim Raynor would like to ally with you to take out the Zerg."
			print "Do you want to ally with Raynor?"
			print "A. Yes"
			print "B. No"

			ally = raw_input("> ")

			if ally == "A":
				return "agree"
			elif ally == "B":
				return "disagree"
			else:
				print "I do not understand your input."
				print "Please respond with 'agree' or 'disagree'."
				return "army"


		elif army == "B":
			print "You choose the melee path."
			print "As you begin to train more zealots, you also send an observer to check on enemy territory."
			print "You find that Kerrigan is making a mass-load of mutalisks, and your zealots will be of no use."
			print "She sends a drone to check out your army, and finds it's only composed of zealots."
			print "She send her mass army of mutalisks to destroy your army and base."
			return "death"


        elif army == "C":
        	print "You choose the ranged path."
        	print "With this you train many stalkers, while researching the ablity to blink."
        	print "With an army of 10 stalkers and your 4 zealots, you charge one of Kerrigan's hive clusters."
        	print "There is a large amount of roaches at the defense, but your stalkers proceed to destroy them with ease."
        	print "Congratulations! You are one step closer to taking out Kerrigan. Next, you must find a way to find Kerrigan herself."
        	print "If you kill Kerrigan, her brood will have no master. They will automatically fight each other, leading to the downfall of the Zerg."
        	return "ranged_path"

        else:
        	print "I do not understand your input."
        	print "Please respond with 'A', 'B', or 'C'."
        	return "first_offense"