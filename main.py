from docxtpl import DocxTemplate

# определяем словарь переменных контекста,  
# которые определены в шаблоне документа DOCX
context = {}
context['group'] = 'ККСО-22-24'

doc = DocxTemplate("template.docx")
# подставляем контекст в шаблон
doc.render(context)
# сохраняем и смотрим, что получилось 
doc.save("generated_docx.docx")