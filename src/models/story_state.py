class StoryState:
    def __init__(self):
        self.chapter = 1
        self.history = []
        self.choices = []
        self.locations = []
        self.npcs_met = []

    def add_event(self, event):
        self.history.append(event)

    def add_choice(self, choice):
        self.choices.append(choice)

    def next_chapter(self):
        self.chapter += 1

    def summary(self):
        return {
            "chapter": self.chapter,
            "events": len(self.history),
            "choices": len(self.choices)
        }
