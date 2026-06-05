
class TXTExporter:
    def export(self,text,path='story.txt'):
        with open(path,'w',encoding='utf-8') as f:
            f.write(text)
