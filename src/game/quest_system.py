
class Quest:
    def __init__(self,name,description):
        self.name=name
        self.description=description
        self.completed=False

class QuestManager:
    def __init__(self):
        self.quests=[]
    def add_quest(self,quest):
        self.quests.append(quest)
    def complete_quest(self,name):
        for q in self.quests:
            if q.name==name:
                q.completed=True
