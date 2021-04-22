#!/usr/bin/env python

from flask import Flask, redirect, url_for, request,jsonify
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
#import numpy as np
import json

app = Flask(__name__)
###----------------------------------------------------
###Why are you using the keyword login in the routing of this funtion. The routing should be relevant to the nature of the function.
### 
###----------------------------------------------------

@app.route('/<imagename>',methods = ['GET'])

###----------------------------------------------------
### Use the function that you created in the other file here. This function is not doing anything that we need 
### 
###----------------------------------------------------



def get_geotagging(imagename):

    exif = Image.open(imagename)
    exif.verify()
    exifdata = exif.getexif()
    
    #return exif
    if not exifdata:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exifdata:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exifdata[idx]:
                    geotagging[val] = exifdata[idx][key]

    jsonstring = json.dumps(geotagging)
    return jsonstring

#image = Image.open(imagename)
#exif = image._getexif()
#geotags = get_geotagging(imagename)
#print(geotags)
    
if __name__=="__main__":
    app.run(debug=True, use_reloader=False)



image=input()
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

def get_exif(imagename):
    image = Image.open(imagename)
    image.verify()
    return image._getexif()




