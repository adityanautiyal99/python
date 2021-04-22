#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import PIL
from PIL import Image
#import pytesseract


# In[ ]:


img = PIL.Image.open("Frame 14.png")


# In[ ]:


wid, hgt = img.size


# In[ ]:


print(str(wid) + "x" + str(hgt))


# In[ ]:


img.show()


# In[ ]:


#2


# In[ ]:


from PIL import Image
from PIL.ExifTags import TAGS


# In[ ]:


with open('Frame 14.png', 'rb') as f:
  contents = f.read()


# In[ ]:


# path to the image or video
imagename = "mypic1.jpeg"

# read the image data using PIL
image = Image.open(imagename)


# In[ ]:


# extract EXIF data
exifdata = img.getexif()


# In[ ]:


# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")


# In[ ]:


#3


# In[ ]:


from PIL import Image
from PIL.ExifTags import TAGS

# open the image
image = Image.open("mypic1.jpeg")

# extracting the exif metadata
exifdata = image.getexif()

# looping through all the tags present in exifdata
for tagid in exifdata:
	
	# getting the tag name instead of tag id
	tagname = TAGS.get(tagid, tagid)

	# passing the tagid to get its respective value
	value = exifdata.get(tagid)
	
	# printing the final result
	print(f"{tagname:25}: {value}")


# In[ ]:


#4


# In[ ]:


pip install Pillow


# In[2]:


from PIL import Image

def get_exif(mypic1):
    image = Image.open('mypic1.jpeg')
    image.verify()
    return image._getexif()

exif = get_exif('Frame 14.png')
print(exif)


# In[ ]:


from PIL.ExifTags import TAGS

def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled

exif = get_exif('mypic1.jpeg')
labeled = get_labeled_exif(exif)
print(labeled)


# In[ ]:





# In[ ]:


###----------------------------------------------------
###This is the funtion you have to call in the flask APP. 
###So you can either put this function inside your Flask file or you can import this function from another Py File
###----------------------------------------------------

from PIL.ExifTags import GPSTAGS

def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

exif = get_exif('Frame 14.png')
geotags = get_geotagging(exif)
print(geotags)


# In[ ]:


###----------------------------------------------------
###This is absolutley correct peice of code. i am not sure why u did not understand this. This is quite clear.
###Once you get Geotagging from the above function then you can use those geotagging in the last funtion to get converted degrees lat long
###----------------------------------------------------

def get_decimal_from_dms(dms, ref):

    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return(lat,lon)


exif = get_exif('mypic1.jpeg')
geotags = get_geotagging(exif)
print(get_coordinates(geotags))


# In[ ]:




