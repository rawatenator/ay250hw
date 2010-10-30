from django.db import models


class Collection(models.Model):
	'''Each upload corresponds to a collection with a unique name, which
	is also its primary key'''
	
	name = models.CharField( max_length=255, unique=True, primary_key=True)
	
	def __str__(self):
		return self.name
	
	
class Entry(models.Model):
	'''Each entry in an upload contains many fields. Once these fields are 
	parsed(done in the view), the values can be stored in an Entry object in
	collumns:
	
		author, ref_tag, author_list, title, journal, volume, pages, year 
	
	the foreign key collection links entries to other entries that were uploaded
	from the same file. In the table, however, this collumn is called: collection_id
	'''
	
	collection = models.ForeignKey(Collection, unique=False,)
	
	title = models.CharField( "title", max_length = 500, unique = False)
	author = models.CharField( "author", max_length = 500, unique = False)
	ref_tag = models.CharField( "ref_tag", max_length = 500, unique = False, default='no ref tag')
	author_list = models.CharField("author_list", max_length=500, unique = False)
	journal = models.CharField("pages", max_length=500, unique = False)
	volume = models.IntegerField('volume',unique = False, blank = True,null = True)
	pages = models.CharField("pages", max_length=500, unique = False)
	year = models.IntegerField('year',unique = False, blank = True, null = True)
	
	
	def __str__(self):
		return self.title
