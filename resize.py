from tkinter import *
from PIL import Image, ImageTk
class Resize(Frame):
# Defining the constructor in the class
	def __init__(self, master): 

		# Calling constructor for method frame 
		Frame.__init__(self, master) 

		# Open and identify the image 
		self.image = Image.open("bg7.png")

		# Create a copy of the image and store in variable 
		self.img_copy = self.image.copy() 

		# Define image using PhotoImage function 
		self.background_image = ImageTk.PhotoImage(self.image) 

		# Create and display the label with the image 
		self.background = Label(self, image=self.background_image) 
		self.background.pack(fill=BOTH,expand=YES) 

		# Bind function resize_background to screen resize 
		self.background.bind('<Configure>',self.resize_background) 

	# Create a function to resize background image 
	def resize_background(self, event): 

		# Get the new width and height for image 
		new_width = event.width 
		new_height = event.height 

		# Resize the image according to new dimensions 
		self.image = self.img_copy.resize((new_width, new_height)) 

		# Define new image using PhotoImage function 
		self.background_image = ImageTk.PhotoImage(self.image) 

		# Change image in the label 
		self.background.configure(image=self.background_image) 