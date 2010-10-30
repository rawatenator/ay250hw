from django import forms
'''these forms are classes that inherit from django.forms class.
They are used to make the forms on the query page and upload page'''

class QueryForm(forms.Form):
	query = forms.CharField(max_length=400)
	
class UploadForm(forms.Form):
	collection_name = forms.CharField(max_length = 255) 
	filename = forms.FileField()