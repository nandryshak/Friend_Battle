from character import *
from magic import *
from sys import exit
import time



class Engine(object):

    def __init__(self, fighter):
        self.enemy = fighter

    
    hero = Character(hero_stats, hero_quotes)
    heromagic = Magic()
    
    print "A wild %s has appeared!" % self.enemy.name
    time.sleep(1)
    print "\'%s\'" % self.enemy.intro
    time.sleep(1)

    def disp_stat(good_guy, bad_guy):
        print ""
        print "HP: %d\t MP: %d" % (good_guy.hp, good_guy.mp)
        print "%s\'s HP: " % bad_guy.name, bad_guy.hp
        print ""

    def disp_magic(protag):
        if protag.lvl < 3:
            print "Which spell?"
            print "\n[H]eal:5MP [S]andpaper:10MP [B]ack"
        else:
            print "Which spell?"
            print "\n[H]eal:5MP [S]andpaper:10MP [C]haos_Dunk:20MP [B]ack"


    while True:

        if hero.hp  > 0:

            my_turn = 1
            while my_turn == 1: #allows me to loop prompt until a satisfactory answer is given

                disp_stat(hero, self.enemy)
                time.sleep(1)
                print "What will you do?"
                print "\n[A]ttack [M]agic M[y]stery [Run]"
                action = raw_input("> ")
                action = action.lower()
                print ""

                if action in ("a", "attack"):
                    hero.attack(self.enemy)
                    time.sleep(1)
                    my_turn = 0 # break out of prompt loop

                elif action in ("m", "magic"):

                    magic_turn = 1
                    while magic_turn == 1:

                        disp_magic(hero)
                        spell = raw_input("> ")
                        spell = spell.lower()
                        print ""

                        if spell in ("h", "heal"):
                            if hero.mp >= heromagic.heal_mp:
                                heromagic.heal(hero)
                                my_turn = 0 # break out of promt loop
                                magic_turn = 0
                            else:
                                print "Not enough MP"

                        elif spell in ("s", "sandpaper"):
                            if hero.mp >= heromagic.sandpaper_mp:
                                heromagic.sandpaper(hero, lucas)
                                my_turn = 0 # break out of prompt loop
                                magic_turn = 0
                            else:
                                print "Not enough MP"

                        elif (spell in ("c", "chaos", "chaos_dunk", "chaos dunk")) and (hero.lvl >= 3):
                            if hero.mp >= heromagic.chaos_mp:
                                heromagic.chaos_dunk(hero, lucas)
                                my_turn = 0 # break out of prompt loop
                                magic_turn = 0
                            else:
                                print "Not enough MP"

                        elif spell in ("b", "back"):
                            magic_turn = 0

                        else:    
                            print "404 error: The spell you are looking for cannot be found."

                elif action in ("r", "run"):
                    hero.run()
                else:
                    print "Please type one of the words listed or simply the letter in the brackets."

        else:
            disp_stat(hero, self.enemy)
            time.sleep(1)
            print "You've died! So sad."
            exit(1)
        print ""

        if self.enemy.hp < 0:
            self.enemy.hp = 0 #that way he doesnt have negative health
        time.sleep(1)    
        disp_stat(hero, self.enemy)
        time.sleep(1)
        if self.enemy.hp > 0:
            print "And now %s!" % self.enemy.name
            time.sleep(1)
            self.enemy.ai(hero)
            if hero.hp < 0:
                hero.hp = 0 # if hero dies, go to 0 health
            time.sleep(1)

        else:
            print "\'%s\'" % self.enemy.outro
            print ""
            print "You win! Brllnt!"
            hero.LevelUp(hero)
            exit(1)


#class FightOrder(object):

 #   fighter = [Character(luke_stats, luke_quotes), Character(dom_stats, dom_quotes)]
    
    
#    def __init__(self, first_fighter):
 #       self.first_fighter = first_fighter

  #  def next_fighter(self, fighter_name):
   #     val = FightOrder.fighter.get(fighter_name)
    #    return val

    #def opening_fighter(self):
     #   return self.next_fighter(self.first_fighter)


#tutorial = FightOrder()
#my_game = Engine(tutorial.fighter[0])
#my_game.play()
a = Engine(Character(luke_stats, luke_quotes))
