from magic import *
from random import randint
import time


luke_stats = {'name': 'Lucas', 'hp': 20, 'mp': 5, 'atkstr': range(1, 3),
              'intro_quote': 'Time to get blasted!', 'outro_quote': 'My leg!'}

luke_quotes = ['Lucas complains at you until your ears bleed!','Lucas beaches you to death!']

dom_stats = {'name': 'Dom', 'hp': 40, 'mp': 20, 'atkstr': range(3, 5),
              'intro_quote': 'How do you play this game again?',
              'outro_quote': 'Whatever, I\'m just gonna move to North Carolina'}

dom_quotes = ['Dom stumbles into you, mumbling apologies and mentioning something about too much to drink',
              'Dom locks you into a bearhug, squeezing the life out of you while mentioning how much he loves you, man',
              'Dom trips and hurls a glass at you. It shatters on your face.',
              'Dom pukes up a ton of blood on you. Like, a metric ton of blood. Then he passes out on the floor.',
              'Dom uses his drunk strength to sock you in the stomach. You fly at least a foot off the ground.']

hero_stats = {'name': 'Lawrence', 'hp': 10, 'mp': 20, 'atkstr': range(4, 7),
              'intro_quote': 'none', 'outro_quote': 'none'}

hero_quotes = ['What a hit!', 'I can\'t believe he took that much damage!']

class Character(object):

    def __init__(self, stats, battle_quotes):
        self.lvl = 1
        self.name = stats['name']
        self.hp = stats['hp']
        self.maxhp = stats['hp']
        self.mp = stats['mp']
        self.atkstr = stats['atkstr']
        self.intro = stats['intro_quote']
        self.outro = stats['outro_quote']
        self.quips = battle_quotes

    def attack(self, opponent):
        print self.quips[randint(0, len(self.quips) - 1)]
        time.sleep(1)
        original_hp = opponent.hp
        strike = self.atkstr[randint(0, len(self.atkstr) - 1)]
        opponent.hp -= strike
        if original_hp - strike < 0:
            damage = original_hp
        else:
            damage = original_hp - opponent.hp
        print "%s takes %d damage!" % (opponent.name, damage)

    def run(self):
        really = raw_input("Are you sure? [Y]es [No]\n> ")
        really = really.lower()
        if really in ("y", "yes"):
            print "You run from the fight. But it doesn\'t end there. The rest of your life you're"
            print "branded a coward; someone who turns tail at the slightest provacation. Your friends"
            print "gradually grow distant from you, and you end your days as an old, bitter man who curses"
            print "the world instead of himself.\n\n\nGAME OVER\n\n\n"
            exit(1)
        elif really in ("n", "no"):
            print "Then why'd you choose Run, silly?"

    def LevelUp(self, old_hero):
        self.lvl = old_hero.lvl + 1
        self.hp = self.lvl * 10
        self.mp = ((self.lvl - 1) * 4) + 10
        self.atkstr = ((self.lvl - 1) * 2) + 5
        print "%s has reached Level %d!" % (self.name, self.lvl)
        time.sleep(1)
        print "HP rose to %d!" % self.hp
        time.sleep(1)
        print "MP rose to %d!" % self.mp
        time.sleep(1)
        print "ATK rose to %d!" % self.atkstr
        if self.lvl == 3:
            time.sleep(1)
            print "%s has learned Chaos_Dunk!" % old_hero.name

    def ai(self, hero):
        if self.name == 'Lucas':
            return self.lucas_ai(hero)
        elif self.name == 'Dom':
            return self.dom_ai(hero)

    def lucas_ai(self, hero):
        lucas_magic = Magic()
        if self.hp < 11:
            outcome = randint(1,3)
            if (outcome == 1) and (self.mp >= lucas_magic.heal_mp):
                lucas_magic.heal(self)
            else:
                self.attack(hero)
        else:
            self.attack(hero)

    def dom_ai(self, hero):
        dom_magic = Magic()
        if (self.hp < 31) and (self.hp > 19):
            outcome = randint(1, 3)
            if (outcome == 1) and (self.mp >= dom_magic.heal_mp):
                dom_magic.heal(self)
            else:
                self.attack(hero)
        elif self.hp < 20:
            outcome1 = randint(1,4)
            if (outcome1 == 1) and (self.mp >= dom_magic.greaterheal_mp):
                dom_magic.greaterheal(self)
            else:
                self.attack(hero)
        else:
            self.attack(hero)
