# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 04:20:02 2019

@author: Prannoy_007
"""
from PIL import Image

img_location = "C:\\Users\\Prannoy_007\\Desktop\\Projects\\TV v Commercials classification\\Training Dataset\\Advertisement\\"
img_bl_location = "C:\\Users\\Prannoy_007\\Desktop\\Projects\\TV v Commercials classification\\Training Dataset\\Advertisement\\Greyscale\\"
img_name_shift = 1
img_orig_shift = 66
for x in range(66, 1507):
    img_location_temp = img_location + str(img_orig_shift) + ".png"
    img = Image.open(img_location_temp).convert('LA')
    img_bl_nameshift = img_bl_location + str(img_name_shift)+".png"
    img.save(img_bl_nameshift)
    img_orig_shift += 1
    img_name_shift += 1
