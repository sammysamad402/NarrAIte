
class StoryMetrics:
    def __init__(self):
        self.chapters=0
        self.words=0
        self.locations=set()
        self.npcs=set()

    def update(self,text,location=None,npc=None):
        self.chapters += 1
        self.words += len(text.split())
        if location:
            self.locations.add(location)
        if npc:
            self.npcs.add(npc)

    def summary(self):
        return {
            'chapters': self.chapters,
            'words': self.words,
            'locations': len(self.locations),
            'npcs': len(self.npcs)
        }
