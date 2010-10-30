#!/usr/bin/env python
# encoding: utf-8
import re

def customize():
	'''sometimes a user may hav emany bibtex files with fields that are not formatted exactly 
	like the fields in the model and view. This function is called in the view on the uploaded
	file to modify the upload and minimize information loss. It uses regex to 
	substitute: re.sub(old,new,string)'''
	
	f = open('Temp/temp.txt', 'r')
	f_read = f.read()
	f.close()
	
	f_read=re.sub('Author', 'author', f_read)
	f_read=re.sub('Title', 'title', f_read)
	f_read=re.sub('Journal', 'journal', f_read)
	f_read=re.sub('Volume', 'volume', f_read)
	f_read=re.sub('Pages', 'pages', f_read)
	f_read=re.sub('Year', 'year', f_read)
	f_read=re.sub('Author_List', 'author_list', f_read)
	
	f = open('Temp/temp.txt', 'w')
	f.write(f_read)
	f.close()