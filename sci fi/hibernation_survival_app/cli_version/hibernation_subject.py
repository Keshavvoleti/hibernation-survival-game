import random
from constants import *

class HibernationSubject:
    def __init__(self):
        self.health = MAX_HEALTH
        self.hand_intact = True
        self.is_hibernating = True

    def cut_hand(self):
        if self.hand_intact:
            damage = random.randint(MIN_HAND_CUT_DAMAGE, MAX_HAND_CUT_DAMAGE)
            self.health -= damage
            self.hand_intact = False
            return f"✂️ Hand amputated! Health -{damage}%!"
        return "❌ Hand already missing!"

    def give_meds(self):
        heal = random.randint(MEDS_HEAL_MIN, MEDS_HEAL_MAX)
        self.health = min(MAX_HEALTH, self.health + heal)
        return f"💉 Health +{heal}%"

    def check_vitals(self):
        return f"📊 Health: {self.health}% | Hand: {'Intact' if self.hand_intact else 'Missing'}"

    def wake_up(self):
        self.is_hibernating = False
        if not self.hand_intact:
            return "🚨 Subject wakes screaming! ❌ Hand missing!"
        return "😊 Subject wakes normally."