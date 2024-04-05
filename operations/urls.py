from django.urls import path
from operations import views

urlpatterns = [
    path('textfiles/', views.text_to_pdf, name="text_to_pdf"),
    path('tablefiles/', views.excel_to_pdf, name="excel_to_pdf"),
    path('presentation/', views.pres_to_pdf, name="presentation_to_pdf"),
    path('photos/', views.image_to_pdf, name="image_to_pdf"),
]
