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

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class': 'form-control'})
		self.fields['description'].widget.attrs.update({'class': 'form-control', 'style': 'resize:none'})
	"""
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 
														 'name': 'name'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
															   'name': 'description', 
															   'style': 'resize: none'}))
	"""														   