from django.urls import path
from . import views

urlpatterns = [
    path('api/<slug:slug>/', views.page_content, name='page_content'),
]
