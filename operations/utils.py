import pythoncom
from docx2pdf import convert as converter_doc
from win32com import client
from pptxtopdf import convert as converter_pptx
from img2pdf import convert as image_converter


class Utils:

    @staticmethod
    def text_to_pdf_conv(file):
        pythoncom.CoInitialize()
        converter_doc(file, f"output/")

    #need to fix
    @staticmethod
    def excel_to_pdf_conv(file):
        pythoncom.CoInitialize()
        excel = client.Dispatch("Excel.Application")
        sheets = excel.Workbooks.Open(f"E:\ConverterProject\{str(file)}")
        work_sheets = sheets.Worksheets[0]
        filename = file.replace("files/", "").split(".")[0]
        work_sheets.ExportAsFixedFormat(0, f"output/{filename}.pdf")

    @staticmethod
    def pres_to_pdf_conv(file):
        pythoncom.CoInitialize()
        converter_pptx(file, f"output/")

    @staticmethod
    def image_to_pdf_conv(file):
        pythoncom.CoInitialize()
        filename = file.replace("files/", "").split(".")[0]
        with open(f"output/{filename}.pdf", "wb") as f:
            f.write(image_converter(file))
