from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

from operations.models import Operation
from operations.utils import Utils
from subscriptions.models import Subscription


# Create your views here.
@login_required(login_url='/auth/login/')
def text_to_pdf(request):
    try:
        if request.method == "POST":
            user = request.user
            sub = Subscription.objects.get(user=user.id)
            sub.operation_decrease()
            file_to_convert = request.FILES.get("formDocFile")
            if not file_to_convert:
                messages.error(request, "Please upload the file")
                return render(request, 'operations/text_to_pdf.html')
            fs = FileSystemStorage()
            try:
                file_extension = Utils.extensions_check(file_to_convert.name, ['.doc', '.docx'])
            except TypeError as e:
                messages.error(request, e)
                return render(request, 'operations/text_to_pdf.html')
            filename = fs.save(f"files/{file_to_convert.name}", file_to_convert)
            Utils.text_to_pdf_conv(filename)
            filename_pure = filename.replace("files/", "").replace(file_extension, '')
            path = f"output/{filename_pure}.pdf"
            operation = Operation(user=request.user, format_from=file_extension, format_to=".pdf",
                                  file_url=path)
            operation.save()
            fs.delete(filename)
            messages.success(request, "Word file was converted to PDF, you can download it in your account")
            return render(request, 'operations/text_to_pdf.html')
    except TypeError as e:
        messages.error(request, e)
        return render(request, 'operations/text_to_pdf.html')
    except ValueError as e:
        messages.error(request, e)
        return render(request, 'operations/text_to_pdf.html')
    return render(request, 'operations/text_to_pdf.html')


@login_required(login_url='/auth/login/')
def excel_to_pdf(request):
    try:
        if request.method == "POST":
            user = request.user
            sub = Subscription.objects.get(user=user.id)
            sub.operation_decrease()
            file_to_convert = request.FILES.get("formExcelFile")
            if not file_to_convert:
                messages.error(request, "Please upload the file")
                return render(request, 'operations/excel_to_pdf.html')
            fs = FileSystemStorage()
            try:
                file_extension = Utils.extensions_check(file_to_convert.name, ['.xlsx'])
            except TypeError as e:
                messages.error(request, e)
                return render(request, 'operations/excel_to_pdf.html')
            filename = fs.save(f"files/{file_to_convert.name}", file_to_convert)
            Utils.excel_to_pdf_conv(filename)
            filename_pure = filename.replace("files/", "").replace(file_extension, '')
            path = f"output/{filename_pure}.pdf"
            operation = Operation(user=request.user, format_from=file_extension, format_to=".pdf",
                                  file_url=path)
            operation.save()
            fs.delete(filename)
            messages.success(request, "Excel file was converted to PDF, you can download it in your account")
            return render(request, 'operations/excel_to_pdf.html')
    except TypeError as e:
        messages.error(request, e)
        return render(request, 'operations/excel_to_pdf.html')
    except ValueError as e:
        messages.error(request, e)
        return render(request, 'operations/excel_to_pdf.html')
    return render(request, 'operations/excel_to_pdf.html')


@login_required(login_url='/auth/login/')
def pres_to_pdf(request):
    try:
        if request.method == "POST":
            user = request.user
            sub = Subscription.objects.get(user=user.id)
            sub.operation_decrease()
            file_to_convert = request.FILES.get("formPresFile")
            if not file_to_convert:
                messages.error(request, "Please upload the file")
                return render(request, 'operations/text_to_pdf.html')
            fs = FileSystemStorage()
            try:
                file_extension = Utils.extensions_check(file_to_convert.name, ['.pptx'])
            except TypeError as e:
                messages.error(request, e)
                return render(request, 'operations/presentation_to_pdf.html')
            filename = fs.save(f"files/{file_to_convert.name}", file_to_convert)
            Utils.pres_to_pdf_conv(filename)
            filename_pure = filename.replace("files/", "").replace(file_extension, '')
            path = f"output/{filename_pure}.pdf"
            operation = Operation(user=request.user, format_from=file_extension, format_to=".pdf",
                                  file_url=path)
            operation.save()
            fs.delete(filename)
            messages.success(request, "PPTX file was converted to PDF, you can download it in your account")
            return render(request, 'operations/presentation_to_pdf.html')
    except TypeError as e:
        messages.error(request, e)
        return render(request, 'operations/presentation_to_pdf.html')
    except ValueError as e:
        messages.error(request, e)
        return render(request, 'operations/presentation_to_pdf.html')
    return render(request, 'operations/presentation_to_pdf.html')


@login_required(login_url='/auth/login/')
def image_to_pdf(request):
    try:
        if request.method == "POST":
            user = request.user
            sub = Subscription.objects.get(user=user.id)
            sub.operation_decrease()
            file_to_convert = request.FILES.get("formImgFile")
            if not file_to_convert:
                messages.error(request, "Please upload the file")
                return render(request, 'operations/img_to_pdf.html')
            fs = FileSystemStorage()
            try:
                file_extension = Utils.extensions_check(file_to_convert.name, ['.png', '.jpg'])
            except TypeError as e:
                messages.error(request, e)
                return render(request, 'operations/img_to_pdf.html')
            filename = fs.save(f"files/{file_to_convert.name}", file_to_convert)
            Utils.image_to_pdf_conv(filename)
            filename_pure = filename.replace("files/", "").replace(file_extension, '')
            path = f"output/{filename_pure}.pdf"
            operation = Operation(user=request.user, format_from=file_extension, format_to=".pdf",
                                  file_url=path, )
            operation.save()
            fs.delete(filename)
            messages.success(request, "Image file was converted to PDF, you can download it in your account")
            return render(request, 'operations/img_to_pdf.html')
    except TypeError as e:
        messages.error(request, e)
        return render(request, 'operations/img_to_pdf.html')
    except ValueError as e:
        messages.error(request, e)
        return render(request, 'operations/img_to_pdf.html')
    return render(request, 'operations/img_to_pdf.html')


@login_required(login_url='/auth/login/')
def pdf_to_docx(request):
    try:
        if request.method == "POST":
            user = request.user
            sub = Subscription.objects.get(user=user.id)
            sub.operation_decrease()
            file_to_convert = request.FILES.get("formPdfDocFile")
            if not file_to_convert:
                messages.error(request, "Please upload the file")
                return render(request, "operations/pdf_to_docx.html")
            fs = FileSystemStorage()
            try:
                file_extension = Utils.extensions_check(file_to_convert.name, [".pdf"])
            except TypeError as e:
                messages.error(request, e)
                return render(request, 'operations/pdf_to_docx.html')
            filename = fs.save(f"files/{file_to_convert.name}", file_to_convert)
            Utils.pdf_to_docx_conv(filename)
            filename_pure = filename.replace("files/", "").replace(file_extension, '')
            path = f"output/{filename_pure}.docx"
            operation = Operation(user=request.user, format_from=file_extension, format_to=".docx",
                                  file_url=path, )
            operation.save()
            fs.delete(filename)
            messages.success(request, "PDF file was converted to Docx, you can download it in your account")
            return render(request, 'operations/pdf_to_docx.html')
    except TypeError as e:
        messages.error(request, e)
        return render(request, 'operations/pdf_to_docx.html')
    except ValueError as e:
        messages.error(request, e)
        return render(request, 'operations/pdf_to_docx.html')
    return render(request, 'operations/pdf_to_docx.html')


def pdf_to_doc(request):
    pass


def pdf_to_img(request):
    pass


class OperationsListView(LoginRequiredMixin, ListView):
    paginate_by = 6
    model = Operation
    template_name = 'operations/user_operations.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Operation.objects.filter(user=user.id).order_by("operation_date")
        return queryset


class OperationsDeleteView(LoginRequiredMixin, DeleteView):
    model = Operation
    success_url = reverse_lazy('operations:operations_list')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Operation was deleted successfully")
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        fs = FileSystemStorage()
        fs.delete(object.file_url)
        messages.success(request, "Operation was deleted successfully")
        return super().delete(request, *args, **kwargs)


@login_required(login_url='/auth/login/')
def operation_download(request, pk):
    operation = get_object_or_404(Operation, pk=pk)
    operation_file = operation.file_url
    return FileResponse(open(operation_file, 'rb'), as_attachment=True)
