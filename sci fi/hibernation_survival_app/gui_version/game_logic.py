import random
from constants import *

class HibernationSubject:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.health = MAX_HEALTH
        self.hand_intact = True
        self.is_hibernating = True
    
    def cut_hand(self):
        if self.hand_intact:
            damage = random.randint(MIN_HAND_CUT_DAMAGE, MAX_HAND_CUT_DAMAGE)
            self.health -= damage
            self.hand_intact = False
            return f"✂️ Hand amputated! (-{damage}% health)"
        return "❌ Hand already missing!"
    
    def give_meds(self):
        heal = random.randint(MEDS_HEAL_MIN, MEDS_HEAL_MAX)
        self.health = min(MAX_HEALTH, self.health + heal)
        return f"💉 Meds administered! (+{heal}% health)"
    
    def get_status(self):
        return {
            "health": self.health,
            "hand": "Intact" if self.hand_intact else "Missing",
            "is_alive": self.health > 0
        }