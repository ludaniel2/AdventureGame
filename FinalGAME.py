from sys import exit
from random import randint

def get_user_input(prompt, permitted_values):
    while True:
        user_input = raw_input(prompt).strip() 
        if user_input in permitted_values:
            return user_input
        print("Invalid Input.")             
 
class Scene(object):
 
    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter")
        exit(1)
 
class Engine(object):
 
    def __init__(self, scene_map):
        self.scene_map = scene_map
 
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
 
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
 
        current_scene.enter()
 
class Death(Scene):
 
    death_quotes = [
        "You just died. Learn to get better.",
        "Congratulations! You just died. Try again.",
        "How did you manage to die? Think wisely."
    ]
 
    def enter(self):
        print(Death.death_quotes[randint(0, len(self.death_quotes)-1)])
        exit(1)
 
class MainRoom(Scene):
 
    def enter(self):
        print("Your name is Tassadar, leader of the Protoss race!")
        print("Your homeland has been attacked by the Zerg race, and it is your job to stop them from taking over your homeland.")
        print("With your will and might, you can save your people and your home.")
        print("However, you must make wise decisions or else you and your people will die.")
        print("\n")
        print("You control: \n\t*24 probes\n\t*4 zealots\n\t*3 stalkers")
        print("The Zerg first swarm your outer core's photon cannons. What would you like to do?")
        print("A. Send 3 of your zealots to fend off the incoming zerglings.")
        print("B. Try to negotiate with Kerrigan to make peace.")
        print("C. Surrender.")
 
        first_step = get_user_input("> ", ["A", "B", "C"])
 
        if first_step == "A":
            print("Congratulations! Your zealots sucessfully slash away at the zerglings and kill them all.")
            print("Kerrigan becomes more agitated, however you have not died and your home still remains.")
            print("Her last attack was very costly. You are now on the offense!")
            return "first_offense"
 
        elif first_step == "B":
            print("As you go to make negotiations with Kerrigan, an enemy hydralisk shoots its acidic goo onto you.")
            print("You start to burn up and dissolve.")
            return "death"
 
        elif first_step == "C":
            print("You send a white flag showing that you plan on surrendering.")
            print("Kerrigan does not accept surrenders and instead rallys her whole swarm to focus on your settlement.")
            print("She kills off your troops and every last probe. She taunts you and kills you last so you can watch your home burn away.")
            return "death"
 
        else:
            print("I do not understand your input.")
            print("Please respond with 'A', 'B', or 'C'.")
            return "main_room"
 
class FirstOffense(Scene):
    def enter(self):
        print("After the last zergling attack, one of your zealots has died.")
        print("You have 3 left.")
        print("You can build up your army now, but can only choose one type of unit.")
        print("Do you want to train: ")
        print("A. More void rays")
        print("B. More zealots")
        print("C. More stalkers")
 
        army = get_user_input("> ", ['A', 'B'])
 
        if army == "A":
            print("You choose the air path.")
            print("You sucessfully build up an army of void rays that are 6 in number.")
            print("As you begin to send out your fleet, a terran marine shows up at the gates.")
            print("He tells you Jim Raynor would like to ally with you to take out the Zerg.")
            print("Do you want to ally with Raynor?")
            print("A. Yes")
            print("B. No")
 
            ally = get_user_input("> ", ['A', 'B'])
 
            if ally == "A":
                return "agree"
            elif ally == "B":
                return "disagree"
            else:
                print("I do not understand your input.")
                print("Please respond with 'agree' or 'disagree'.")
                return "army"
 
 
        elif army == "B":
            print("You choose the melee path.")
            print("As you begin to train more zealots, you also send an observer to check on enemy territory.")
            print("You find that Kerrigan is making a mass-load of mutalisks, and your zealots will be of no use.")
            print("She sends a drone to check out your army, and finds it's only composed of zealots.")
            print("She send her mass army of mutalisks to destroy your army and base.")
            return "death"
 
 
        elif army == "C":
            print("You choose the ranged path.")
            print("With this you train many stalkers, while researching the ablity to blink.")
            print("With an army of 10 stalkers and your 4 zealots, you charge one of Kerrigan's hive clusters.")
            print("There is a large amount of roaches at the defense, but your stalkers proceed to destroy them with ease.")
            print("Congratulations! You are one step closer to taking out Kerrigan. Next, you must find a way to find Kerrigan herself.")
            print("If you kill Kerrigan, her brood will have no master. They will automatically fight each other, leading to the downfall of the Zerg.")
            return "ranged_path"
 
        else:
            print("I do not understand your input.")
            print("Please respond with 'A', 'B', or 'C'.")
            return "first_offense"
 
class RangedPath(Scene):
 
    def enter(self):
        print("You have created a mass army of stalkers that can blink.")
        print("You send your stalkers and the couple zealots you have to attack")
        print("Along the way, another Protoss tribe's probe comes along with a message.")
        print("It tells you that it has a bomb that will self-explode unless you defuse it correctly.")
        print("The code is just 1 digit long, from 1 to 5. You have 4 guesses.")
        print("What do you enter?")
 
        code = randint(1,5)    
        guesses = 4
        permitted = [str(k) for k in range(1,6)]  
        your_guess = get_user_input("Number: ", permitted)
 
        while int(your_guess) != code and guesses > 0:
            guesses -=1
            print("ERRRRR! Incorrect. You only have {} more guesses".format(guesses))
            your_guess = get_user_input("Number: ", permitted)
 
        if int(your_guess) == code:
            print("That is the right code. You sucessfully defuse the bomb.")
            print("You now have a large army, and send it to the main hive.")
            print("There are two hatcheries here. Each is in its own section.")
            print("You only have time to attack one hatchery. You must choose")
            print("the one Kerrigan is in or you will fail and get flanked by enemy units.")
            print("Which one do you take?")
            print("A. 1")
            print("B. 2")
        else:
            print("You ran out of tries. The probe self-expodes, killing you and your army.")
            return "death"
 
        hatchery = randint(1,2)
        guess = get_user_input("Hatchery #: ", ['1', '2'])

        if int(guess) != hatchery:
            print("You have chosen the wrong hatchery.")
            print("The other hatchery sends troops to flank, and all of your and Raynor's troops die.")
            return "death"
        else:
            print("You have chosen the right one! Your void rays obliterate every last creature in sight.")
            print("Kerrigan is the last one remaining, and you kill her yourself.")
            print("Enemy Zerg are now fighting each other, leaving the Zerg to fall and you victorious.")
            return "finished"
           
class Agree(Scene):
 
    def enter(self):
        print("So you agree to ally with Raynor.")
        print("Good choice. He sends over an army of medivacs, marines, and marauders.")
        print("Your void rays and his army wipe out the hive cluster.")
        print("Your next step is to find Kerrigan. If you take out Kerrigan, the Zerg will clash within and fall.")
        print("You know she is hiding somewhere inside the main hive.")
        print("You now have a large army, and send it to the main hive.")
        print("There are two hatcheries here. Each is in its own section.")
        print("You only have time to attack one hatchery. You must choose the one Kerrigan is in or you will fail and get flanked by enemy units.")
        print("Which one do you take?")
        print("A. 1")
        print("B. 2")
       
        hatchery = randint(1,2)
        guess = get_user_input("Hatchery #: ", ['1', '2'])
 
        if int(guess) != hatchery:
            print("You have chosen the wrong hatchery.")
            print("The other hatchery sends troops to flank, and all of your and Raynor's troops die.")
            return "death"
        else:
            print("You have chosen the right one! Your void rays obliterate every last creature in sight.")
            print("Kerrigan is the last one remaining, and you kill her yourself.")
            print("Enemy Zerg are now fighting each other, leaving the Zerg to fall and you victorious.")
            return "finished"
 
class Disagree(Scene):
 
    def enter(self):
        print("You disagree to all with Raynor.")
        print("Bad choice! As you send your void rays to attack the hive cluster, an army of burrowed hydralisks and zerglings stealthily creep to your base.")
        print("They wipe out every last probe and structure, leaving you left to witness the destruction.")
        print("After, they kill you.")
        return "death"
 
class Finished(Scene):
 
    def enter(self):
        print("Congragulations! Your leadership and skill saved your people and home.")
        print("You have won the game!")
 
class Map(object):
 
    scenes = {
        'main_room': MainRoom(),
        'first_offense': FirstOffense(),
        'ranged_path': RangedPath(),
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


a_map = Map('main_room')
a_game = Engine(a_map)
a_game.play()