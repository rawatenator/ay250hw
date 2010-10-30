## RISHI RAWAT, HW6 AY250

from enthought.traits.api import *
from enthought.traits.ui.api import *
from enthought.traits.ui.menu import NoButtons
from mpl_figure_editor import MPLFigureEditor  #this editor is from code.enthought.com/.../traits/.../tutorials/traits_ui_scientific_app.html; I have saved the file locally to treat it as a module
from matplotlib.figure import Figure
from scipy import *
import wx
from PIL import Image
from cStringIO import StringIO
from urllib2 import urlopen
from yahoo.search.image import ImageSearch
import ImageFilter


class search(HasTraits):
	'''A search object has a gui which allows users to edit a picture returned from a search query;
	yahoo search image API is used to fetch an image;
	A matplotlib editor is used with traits to display the picture. The editor was borrowed from the tutorial at: http://code.enthought.com/projects/traits/docs/html/tutorials/traits_ui_scientific_app.html'''
	
	#TEXT FIELDS DEFINED:
	text_entry_field= String()
	text_entry_submit = Button()
	imageURL = String()
	
	#EDITING METHODS(BUTTONS):
	rotate90 = Button()				
	blur = Button()
	sharpen=Button()
	emboss=Button()
	
	#This is the matplotlib figure
	figure = Instance(Figure, ())
	
	#WHEN THE USER PRESSES THE text_entry_submit BUTTON:
	def _text_entry_submit_fired(self):
		'''action for button; when fired, button executes 3 methods:
			1.) get_url_of_image(input = text_entry_field, output = url for yahoo search's first image result)
			2.) get_image_from_url(input=url of image, action = saves current_image.png in directory)
			3.) image_show(input=self, the file "current_image.png" in the directory; output=sets the image on the MPL canvas and uses wx to redraw/update plot)'''
		
		url = get_url_of_image(str(self.text_entry_field))
		self.imageURL = url
		get_image_from_url(url)
		image_show(self)
	
	#EDITING METHODS:
	def _rotate90_fired(self):
		image = Image.open("current_image.png")
		image.rotate(90).save('current_image.png')
		image_show(self)

	def _blur_fired(self):
		image = Image.open("current_image.png")
		image.filter(ImageFilter.BLUR).save('current_image.png')
		image_show(self)
	
	def _sharpen_fired(self):
		image = Image.open("current_image.png")
		image.filter(ImageFilter.SHARPEN).save('current_image.png')
		image_show(self)
	
	def _emboss_fired(self):
		image = Image.open("current_image.png")
		image.filter(ImageFilter.EMBOSS).save('current_image.png')
		image_show(self)
	
	#DEFINING THE VIEW, GROUPING TO IMPROVE ASTHETICS	
	view = View(
				Group(
					Group(	Item('text_entry_field',show_label=False),
							Item('text_entry_submit',show_label = False),
							label = 'input',
							show_border = True),
						
					Group(	Item('imageURL',show_label=False,style='readonly'),
							label='imageURL',
							show_border = True),
				
					Group(	Item('figure',  editor=MPLFigureEditor(),show_label=False),
							label = 'Image Display',
							show_border = True),
						
					Group(	Item('rotate90',show_label=False),
							Item('blur',show_label=False),
							Item('sharpen',show_label=False),
							Item('emboss',show_label=False),
							label = 'Editing Options',
							show_border = True,
							
							orientation= 'horizontal', 
							layout='flow',
							show_labels=False),
						),  
				width = 500,
				height = 500,
				resizable=True  )
				
	

#FUNCTION THAT DISPLAYS A LOCALLY SAVED IMAGE ON THE MPL PLOT
def image_show(self):
	'''Opens 'current_image.png' and displays on plot;
	image_show(input=self, the file "current_image.png" in the directory; output=sets the image on the MPL canvas and uses wx to redraw/update plot)'''
	image = Image.open("current_image.png")
	axes = self.figure.add_subplot(111)
	axes.imshow(image)
	wx.CallAfter(self.figure.canvas.draw)

#GETS A URL USING THE YAHOO API
def get_url_of_image(query_string):
	'''gets an image from a yahoo image search of "query string", returns a url'''
	
	srch = ImageSearch(app_id="YahooDemo", query='%s'%query_string)
	srch.results = 1
	for each in srch.parse_results():
		url = str(each.Url)
	return url

#SAVES AN IMAGE TO DISK FROM A URL
def get_image_from_url(url):
	'''get_image_from_url(url) takes a url, reads it into a PIL Image object, saves the image as current_image.png'''
	image = urlopen(url)
	im2 = StringIO(image.read())
	im = Image.open(im2).transpose(Image.FLIP_TOP_BOTTOM)
	im.save('current_image.png')
	

#STARTS THE APP
search().configure_traits()






