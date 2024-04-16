from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('verification/<str:uidb64>/', views.email_verify, name='email_verify'),
    path('user_details/',views.UserDetails.as_view(),name="user_details")
]
