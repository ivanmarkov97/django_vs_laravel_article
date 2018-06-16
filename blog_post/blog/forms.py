from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"image",
			"name",
			"description"
		]
	"""
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 
														 'name': 'name'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
															   'name': 'description', 
															   'style': 'resize: none'}))
	"""														   