from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),  #new
    path('<int:pk>/', views.detail, name='detail'),  #detail
    path('create/', views.create, name='create'),  #create
    # path('edit/<int:pk>/', views.edit, name='edit'),  #edit
    path('delete/<int:pk>/', views.delete, name='delete'),  #delete
    path('update/<int:pk>/', views.update, name='update'),  #update


]