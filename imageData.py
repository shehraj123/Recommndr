import webbrowser
from PIL import Image, ImageEnhance
from PIL.ExifTags import TAGS

img_file = 'nature.jpg'
image = Image.open(img_file)

def Luminosity(image):
	image_data = image.getdata()
	Luminosity = []
	for tup in image_data:
		r, g, b = tup
		pixel_Luminosity =  (r+r+b+g+g+g)/6
		Luminosity.append(pixel_Luminosity)
	value = sum(Luminosity)/len(Luminosity)
	value = round((value/255)*100, 2)
	return value

def Saturation(image):
	image_data = image.getdata()

	rg = [r - g for r,g,b in image_data]
	yb = [0.5*(r+g) - b for r,g,b in image_data]
	rgMean = sum(rg)/len(rg)
	ybMean = sum(yb)/len(yb)
	rgSDev = ((sum([(val - rgMean)**2 for val in rg]))/len(rg))**0.5
	ybSDev = ((sum([(val - ybMean)**2 for val in yb]))/len(yb))**0.5

	rgybMean = (rgMean**2 + ybMean**2)**0.5
	rgybSDev = (rgSDev**2 + ybSDev**2)**0.5

	value = rgybSDev = 0.3*rgybMean
	value = round(((value/7)*100), 2)
	return value
