from django.urls import path
from operations import views

urlpatterns = [
    path('textfiles/', views.text_to_pdf, name="text_to_pdf"),
    path('tablefiles/', views.excel_to_pdf, name="excel_to_pdf"),
    path('presentation/', views.pres_to_pdf, name="presentation_to_pdf"),
    path('photos/', views.image_to_pdf, name="image_to_pdf"),
    path('list/', views.OperationsListView.as_view(), name="operations_list"),
    path('delete/<str:pk>/', views.OperationsDeleteView.as_view(), name="operations_delete"),
    path('download/<str:pk>/', views.operation_download,name="operations_download"),
]
