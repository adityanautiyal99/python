from flask import Flask, redirect, url_for, request,jsonify
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
import json

imagename=input()

def get_exif(imagename):
    image = Image.open(imagename)
    image.verify()
    return image._getexif()

#exif = get_exif(imagename)

#print(data)

def get_geotagging(image_name):
    
    image = Image.open(image_name)
    image.verify()
    exif = image._getexif()
    #if not exif:
        #raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    #jsonstring = json.dumps(geotagging)
    #return jsonstring
    return geotagging

# image = Image.open(imagename)
# exif = image._getexif()
geotags = get_geotagging(imagename)
print(geotags)
