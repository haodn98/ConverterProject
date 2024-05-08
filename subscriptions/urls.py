from django.urls import path
from subscriptions import views

urlpatterns = [
    path('payment/', views.payment_taking, name="payment"),

]
