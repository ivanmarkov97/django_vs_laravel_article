from django.urls import path, include
from . import views

urlpatterns = [
	path('create/<int:post_id>', views.create_comment, name='create_comment'),
]
