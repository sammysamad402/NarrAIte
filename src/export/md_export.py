
class MarkdownExporter:
    def export(self,text,path='story.md'):
        with open(path,'w',encoding='utf-8') as f:
            f.write(text)
