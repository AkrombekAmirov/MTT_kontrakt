from os.path import join, dirname, exists
from docx.shared import Inches, Pt
from datetime import datetime
from docx2pdf import convert
from docx import Document
from os import remove
from os.path import join, dirname


async def replace_text(paragraph, old_text, new_text, font_size=None, bold=True, underline=False):
    for run in paragraph.runs:
        if old_text in run.text:
            run.text = run.text.replace(old_text, new_text)
            if font_size:
                run.font.size = Pt(font_size)
            if bold:
                run.font.bold = True
            if underline:
                run.font.underline = True


async def process_document(address, name):
    doc = Document(join(dirname(__file__), "ariza.docx"))
    for paragraph in doc.paragraphs:
        if "ADDRESS" in paragraph.text:
            await replace_text(paragraph, "ADDRESS", address)
        if "NAME" in paragraph.text:
            await replace_text(paragraph, "NAME", name)
        if "DATEFULL" in paragraph.text:
            await replace_text(paragraph, "DATEFULL", f"{datetime.now().strftime('%d.%m.%Y')}    {name}")
        doc.save(join(dirname(__file__), f"file_ariza\\{name}.docx"))
