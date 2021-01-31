from django.urls import path
import website.views as views 

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>', views.post, name='posts'),
]
