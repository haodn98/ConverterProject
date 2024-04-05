import os

from django.http import FileResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

from operations.models import Operation
from operations.utils import Utils


# Create your views here.

def text_to_pdf(request):
    if request.method == "POST":
        file_to_convert = request.FILES.get("formDocFile")
        if not file_to_convert:
            messages.error(request, "Please upload the file")
            return render(request, 'operations/text_to_pdf.html')
        fs = FileSystemStorage()
        allowed_extensions = ['.doc', '.docx', '.txt']
        file_extension = os.path.splitext(file_to_convert.name)[1]
        if file_extension not in allowed_extensions:
            messages.error(request, "Wrong format!Please use '.doc', '.docx', '.txt' formats")
            return render(request, 'operations/text_to_pdf.html')
        # operation = Operation(user=request.user, format_from=file_extension, format_to="pdf")
        filename = fs.save(f"files/{file_to_convert.name}", file_to_convert)
        Utils.text_to_pdf_conv(filename)
        filename_pure = filename.replace("files/", "").replace(file_extension,'')
        path = f"output/{filename_pure}.pdf"
        print(path)
        fs.delete(filename)
        messages.success(request, "Word file was converted to PDF, you can download it in your account")
        return render(request, 'operations/text_to_pdf.html')
    return render(request, 'operations/text_to_pdf.html')


def excel_to_pdf(request):
    if request.method == "POST":
        file_to_convert = request.FILES.get("formExcelFile")
        if not file_to_convert:
            messages.error(request, "Please upload the file")
            return render(request, 'operations/excel_to_pdf.html')
        fs = FileSystemStorage()
        allowed_extensions = ['.xlsx']
        file_extension = os.path.splitext(file_to_convert.name)[1]
        if file_extension not in allowed_extensions:
            messages.error(request, "Wrong format! Please use '.xlsx' format")
            return render(request, 'operations/excel_to_pdf.html')
        # operation = Operation(user=request.user, format_from=file_extension, format_to="pdf")
        filename = fs.save(f"files/{file_to_convert.name}", file_to_convert)
        Utils.excel_to_pdf_conv(filename)
        filename_pure = filename.replace("files/", "").replace(file_extension, '')
        path = f"output/{filename_pure}.pdf"
        fs.delete(filename)
        messages.success(request, "Excel file was converted to PDF, you can download it in your account")
        return render(request, 'operations/excel_to_pdf.html')
    return render(request, 'operations/excel_to_pdf.html')


def pres_to_pdf(request):
    if request.method == "POST":
        file_to_convert = request.FILES.get("formPresFile")
        if not file_to_convert:
            messages.error(request, "Please upload the file")
            return render(request, 'operations/text_to_pdf.html')
        fs = FileSystemStorage()
        allowed_extensions = ['.pptx']
        file_extension = os.path.splitext(file_to_convert.name)[1]
        if file_extension not in allowed_extensions:
            messages.error(request, "Wrong format! Please use '.pptx' formats")
            return render(request, 'operations/presentation_to_pdf.html')
        # operation = Operation(user=request.user, format_from=file_extension, format_to="pdf")
        filename = fs.save(f"files/{file_to_convert.name}", file_to_convert)
        Utils.pres_to_pdf_conv(filename)
        filename_pure = filename.replace("files/", "").replace(file_extension, '')
        path = f"output/{filename_pure}.pdf"
        fs.delete(filename)
        messages.success(request, "PPTX file was converted to PDF, you can download it in your account")
        return render(request, 'operations/presentation_to_pdf.html')
    return render(request, 'operations/presentation_to_pdf.html')


def image_to_pdf(request):
    if request.method == "POST":
        file_to_convert = request.FILES.get("formImgFile")
        if not file_to_convert:
            messages.error(request, "Please upload the file")
            return render(request, 'operations/img_to_pdf.html')
        fs = FileSystemStorage()
        allowed_extensions = ['.png', '.jpg']
        file_extension = os.path.splitext(file_to_convert.name)[1]
        if file_extension not in allowed_extensions:
            messages.error(request, "Wrong format! Please use '.png', '.jpg' formats")
            return render(request, 'operations/presentation_to_pdf.html')
        # operation = Operation(user=request.user, format_from=file_extension, format_to="pdf")
        filename = fs.save(f"files/{file_to_convert.name}", file_to_convert)
        Utils.image_to_pdf_conv(filename)
        filename_pure = filename.replace("files/", "").replace(file_extension, '')
        path = f"output/{filename_pure}.pdf"
        fs.delete(filename)
        messages.success(request, "Image file was converted to PDF, you can download it in your account")
        return render(request, 'operations/img_to_pdf.html')
    return render(request, 'operations/img_to_pdf.html')


def pdf_to_doc(request):
    pass


def pdf_to_img(request):
    pass
