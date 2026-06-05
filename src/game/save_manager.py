
import json

class SaveManager:
    def save(self,data,path='save_game.json'):
        with open(path,'w') as f:
            json.dump(data,f,indent=2)

    def load(self,path='save_game.json'):
        with open(path,'r') as f:
            return json.load(f)
