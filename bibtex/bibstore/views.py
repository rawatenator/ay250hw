# Create your views here.
from django.template import RequestContext
from bibstore.models import Collection, Entry
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from bibstore.forms import QueryForm, UploadForm
from bibparse import parse_bib
import sqlite3
from bibstore.customize import customize

def collection_view(request, template_name="home.html"):
	'''gets all of the collection objects 
	and passes them to to the template 
	called template_name via all_collections'''
	all_collections = Collection.objects.all()
	return render_to_response(template_name, 
							{'collections' : all_collections}, 
							context_instance = RequestContext(request))


def query(request):
	''' when a user goes to /query, this function is called.
	It either generates an empty form(via the else when the request is not POST), 
	or responds to a Post request which is made when the form is submitted
	
	using the if/else technique allows one function to control the same page
	depending on whether or not the user has submitted the form
	
	To generate search results, search is performed after the "WHERE" in "SELECT * FROM
	x WHERE "...
	
	Resuls are sent to the template
	'''
	if request.method == 'POST':
		form = QueryForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user_search_query = cd["query"]
			
			resultlist = Entry.objects.extra(where=[user_search_query])	
			
			return render_to_response('query.html', {'form':form, 'search_results': resultlist})
	else:
		form = QueryForm()
	return render_to_response('query.html', {'form':form})


def upload(request):
	'''function controls upload based on whether or not the request type is POST(see explanation for query above)
	
	Getting info from file: upon POST, the file to be uploaded is written to the server in chunks(in case it's a 
	large files). The collection name is also storred, and used to make a new Collection object.
	
	Saving info: The function customize(from customize.py located in bibtex/bibstore) is called to do text 
	replacements via regex. Finally, the parse_bib method from bibparse.py is called on the file to make iterable 
	objects corresponding to indidual entries. For each object, a new Entry object is made and defined. It is also 
	associated with the newly made Collection object'''
	
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			
			f = request.FILES['filename']
			collection_name = form.cleaned_data['collection_name']
			destination = open('Temp/temp.txt', 'wb+')
			for chunk in f.chunks():
				destination.write(chunk)
			destination.close()
			
			#the customize funciton in bibstore.customize 
			#allows users to quickly customize the file reading options
			#so that fields can be read in the parser
			# in this case, the function change case of all Entry attributes to lower case
			customize()
			f_parsed = parse_bib('Temp/temp.txt')			
			c = Collection()
			c.name = collection_name
			c.save()
			for entry in f_parsed:
				d = Entry()
				d.collection = c
				
				entry_column_names = ['ref_tag','author_list','author','journal', 'volume','pages', 'year', 'title']
				for column in entry_column_names:
					if column in entry.data:
						d.__setattr__(column, entry.data[column])
				d.save()
					
			return HttpResponseRedirect('/')
	
	else:
		form = UploadForm()
	return render_to_response('upload.html', {'form':form})

