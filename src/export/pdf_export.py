
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

class PDFExporter:
    def export(self,text,path='story.pdf'):
        doc=SimpleDocTemplate(path)
        styles=getSampleStyleSheet()
        doc.build([Paragraph(text,styles['BodyText'])])
