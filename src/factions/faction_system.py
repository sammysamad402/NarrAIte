
class Faction:
    def __init__(self,name):
        self.name=name

class ReputationSystem:
    def __init__(self):
        self.reputation={}

    def add_rep(self,faction,points):
        self.reputation[faction]=self.reputation.get(faction,0)+points
