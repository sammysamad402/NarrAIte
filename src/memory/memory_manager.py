
class MemoryManager:
    def __init__(self):
        self.events=[]
    def add_event(self,event):
        self.events.append(event)
    def get_history(self):
        return '\n'.join(self.events)
