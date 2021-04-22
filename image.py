#!/usr/bin/env python
# from PIL.ExifTags import TAGS
# from PIL import Image
# from PIL.ExifTags import GPSTAGS
# from geopy.geocoders import Here
# import os
# import requests

# def get_exif(filename):
#     image = Image.open(filename)
#     image.verify()
#     return image._getexif()

# exif = get_exif('coldwar.jpg')
# # print(exif)

# def get_labeled_exif(exif):
#     labeled = {}
#     for (key, val) in exif.items():
#         labeled[TAGS.get(key)] = val

#     return labeled

# # exif = get_exif('coldwar.jpg')
# labeled = get_labeled_exif(exif)
# # print(labeled)

# def get_geotagging(exif):
#     if not exif:
#         raise ValueError("No EXIF metadata found")

#     geotagging = {}
#     for (idx, tag) in TAGS.items():
#         if tag == 'GPSInfo':
#             if idx not in exif:
#                 print(idx)
#                 return ValueError("No EXIF geotagging found")

#         for (key, val) in GPSTAGS.items():
#             if key in exif[idx]:
#                 geotagging[val] = exif[idx][key]

#     return geotagging

# # exif = get_exif('adi.JPEG')
# # geotags = get_geotagging(exif)
# # print(geotags)

# def get_decimal_from_dms(dms, ref):
#     # dms=list(map(int, str(dms)))
#     # ref=list(map(int, str(ref)))
#     degrees = dms[0][0] / dms[0][1]
#     minutes = dms[1][0] / dms[1][1] / 60.0
#     seconds = dms[2][0] / dms[2][1] / 3600.0

#     if ref in ['S', 'W']:
#         degrees = -degrees
#         minutes = -minutes
#         seconds = -seconds

#     return round(degrees + minutes + seconds, 5)

# def get_coordinates(geotags):
#     print("hi")
#     print(geotags)
#     lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

#     lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

#     return (lat,lon)


# # exif = get_exif('adi.JPEG')
# geotags = get_geotagging(exif)
# print(get_coordinates(geotags))
# import os
# import requests

# def get_location(geotags):
#     coords = get_coordinates(geotags)

#     uri = 'https://revgeocode.search.hereapi.com/v1/revgeocode'
#     headers = {}
#     params = {
#         'apiKey': os.environ['API_KEY'],
#         'at': "%s,%s" % coords,
#         'lang': 'en-US',
#         'limit': 1,
#     }

#     response = requests.get(uri, headers=headers, params=params)
#     try:
#         response.raise_for_status()
#         return response.json()

#     except requests.exceptions.HTTPError as e:
#         print(str(e))
#         return {}

# # exif = get_exif('adi.JPEG')
# # geotags = get_geotagging(exif)
# location = get_location(geotags)

# # print(location['items'][0]['address']['label'])


# # exif = get_exif('adi.JPEG')
# # geotags = get_geotagging(exif)
# # coords = get_coordinates(geotags)
# # geocoder = Here(apikey=os.environ['API_KEY'])
# # print(geocoder.reverse("%s,%s" % coords))

# import cv2
# import numpy as np

# im = cv2.imread("adi.JPEG")
# gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray, (5, 5), 0)
# _, bin = cv2.threshold(gray,120,255,1) # inverted threshold (light obj on dark bg)
# bin = cv2.dilate(bin, None)  # fill some holes
# bin = cv2.dilate(bin, None)
# bin = cv2.erode(bin, None)   # dilate made our shape larger, revert that
# bin = cv2.erode(bin, None)
# bin, contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# rc = cv2.minAreaRect(contours[0])
# box = cv2.boxPoints(rc)
# for p in box:
#     pt = (p[0],p[1])
#     print(pt)
#     cv2.circle(im,pt,5,(200,0,0),2)
# cv2.imshow("plank", im)
# cv2.waitKey()

import cv2 as cv
import numpy as np

im = cv.imread("adi.JPEG")
gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (5, 5), 0)
_, bin = cv.threshold(gray,120,255,1) # inverted threshold (light obj on dark bg)
bin = cv.dilate(bin, None)  # fill some holes
bin = cv.dilate(bin, None)
bin = cv.erode(bin, None)   # dilate made our shape larger, revert that
bin = cv.erode(bin, None)
contours, hierarchy = cv.findContours(bin, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

rc = cv.minAreaRect(contours[0])
box = cv.boxPoints(rc)
for p in box:
    pt = (p[0],p[1])
    print(pt)
    cv.circle(im,pt,5,(200,0,0),2)
cv.imshow("plank", im)
cv.waitKey()
