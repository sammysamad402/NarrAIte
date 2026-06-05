
import json
class JSONBackup:
    def save(self,data,path='backup.json'):
        with open(path,'w') as f:
            json.dump(data,f,indent=2)
