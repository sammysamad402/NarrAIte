
class RelationshipManager:
    def increase(self,npc,points=1):
        npc.relationship += points

    def decrease(self,npc,points=1):
        npc.relationship -= points
