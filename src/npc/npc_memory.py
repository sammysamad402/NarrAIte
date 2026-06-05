
class NPCMemory:
    def remember(self,npc,event):
        npc.memory.append(event)

    def recall(self,npc):
        return npc.memory
