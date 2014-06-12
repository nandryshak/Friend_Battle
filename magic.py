from random import randint
import time

class Magic(object):

    def __init__(self):
        self.heal_mp = 5
        self.greaterheal_mp = 10
        self.sandpaper_mp = 10
        self.chaos_mp = 20

    def heal(self,caster):
        original_hp = caster.hp
        caster.hp += 5
        if caster.hp > caster.maxhp:
            caster.hp = caster.maxhp
        print "%s takes out a bandage and some anitseptic ointment and treats one of his wounds for %d health!" % (caster.name, caster.hp - original_hp)
        caster.mp -= self.heal_mp

    def greaterheal(self,caster):
        original_hp = caster.hp
        caster.hp += 10
        if caster.hp > caster.maxhp:
            caster.hp = caster.maxhp
        print "%s set his broken bone and applies a splint, restoring %d health!" % (caster.name, caster.hp - original_hp)
        caster.mp -= self.heal_mp

    def sandpaper(self, caster, rubbed):
        original_hp = rubbed.hp
        rubbed.hp -= 10
        if original_hp - 10 < 0:
            damage = original_hp
        else:
            damage = original_hp - rubbed.hp
        print "%s acts really abraisive towards %s and it kind of hurts his feelings.\n" % (caster.name, rubbed.name)
        time.sleep(1)
        print "%s takes %d points of emotional damage!\n(Note: Emotional Damage is the same as normal damage.)" % (rubbed.name, damage)
        caster.mp -= self.sandpaper_mp

    def chaos_dunk(self, caster, slammed):
        original_hp = slammed.hp
        slammed.hp -= 50
        if original_hp - 50 < 0:
            damage = original_hp
        else:
            damage = original_hp - slammed.hp
        print "There were no survivors. You monster."
        caster.mp -= self.chaos_mp
