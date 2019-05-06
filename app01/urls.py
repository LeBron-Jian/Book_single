from django.urls import path, re_path
from app01 import views

app_name = 'app01'

urlpatterns = [
    path('books/', views.books, name='books'),
    path('addbooks/', views.addbooks, name='addbooks'),
    path('<int:id>/delete', views.delbook, name='delbook'),
    path('<int:id>/change/', views.changebook, name='changebook'),
    path('query/', views.query, name='query'),
    path('test/', views.test, name='test')
]

