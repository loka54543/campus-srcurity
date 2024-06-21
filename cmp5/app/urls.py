from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('visitor/', views.visitor_view, name='visitor'),
    path('visitor_dashboard/', views.visitor_dashboard, name='visitor_dashboard'),
    path('qr/', views.qr_page, name='qr_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.login, name='logout'),
    path('qr-code-generator/', views.qr_code_generator, name='qr_code_generator'),
    path('submit_report/', views.submit_report, name='submit_report'),  # Ensure this line is correct

]
