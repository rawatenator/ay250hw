from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
	
	#Top of directory : /
	(r'^$', 'bibstore.views.collection_view'),
	
	# /query
	(r'^query/$','bibstore.views.query'),
	
	#/upload
	(r'^upload/$','bibstore.views.upload'),



)
