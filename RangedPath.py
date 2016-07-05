class RangedPath(Scene):

	def enter(self):
        print "You have created a mass army of stalkers that can blink."
        print "You send your stalkers and the couple zealots you have to attack"
        print "Along the way, another Protoss tribe's probe comes along with a message."
        print "It tells you that it has a bomb that will self-explode unless you defuse it correctly."
        print "The code is just 1 digit long, from 0,5. You have 3 guesses."
        print "What do you enter?"

        code = randint(0,5)
        guesses = 0
        your_guess = raw_input("Number: ")

        while int(your_guess) != code and guesses < 3:
    		guesses +=1
    		print "ERRRRR! Incorrect. You only have %d more guesses" %guesses
    		raw_input("Number: ")

        if int(your_guess) == code:
        	print "That is the right code. You sucessfully defuse the bomb."
        	print "You now have a large army, and send it to the main hive."
			print "There are two hatcheries here. Each is in its own section." 
			print "You only have time to attack one hatchery. You must choose"
			print "the one Kerrigan is in or you will fail and get flanked by enemy units."
    		print "Which one do you take?"
    		print "A. 1"
    		print "B. 2"
    	else:
    		print "You ran out of tries. The probe self-expodes, killing you and your army."
    		return "death"

    		hatchery = randint(1,2)
    		guess = raw_input("Hatchery #: ")

    		if int(guess) != hatchery:
    			print "You have chosen the wrong hatchery."
    			print "The other hatchery sends troops to flank, and all of your and Raynor's troops die."
    			return "death"
    		else:
    			print "You have chosen the right one! Your void rays obliterate every last creature in sight."
    			print "Kerrigan is the last one remaining, and you kill her yourself."
    			print "Enemy Zerg are now fighting each other, leaving the Zerg to fall and you victorious."
    	   	    return "finished"
    		

