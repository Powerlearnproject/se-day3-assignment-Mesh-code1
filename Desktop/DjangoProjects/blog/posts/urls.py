from django.urls import path

from posts import views


urlpatterns = [
    path('firstview/', views.viewname),


]