from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('index/', views.index, name='index'),
	path('<int:post_id>/', views.post, name='post'),
	path('create/', views.create_post, name='create_post'),
]
