from docxtpl import DocxTemplate
from datetime import datetime

context = {}
context['year'] = datetime.now().year

doc = DocxTemplate("template.docx")
doc.render(context)
doc.save("generated_docx.docx")
