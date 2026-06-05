
class AchievementManager:
    def __init__(self):
        self.achievements=set()
    def unlock(self,name):
        self.achievements.add(name)
    def get_all(self):
        return list(self.achievements)
