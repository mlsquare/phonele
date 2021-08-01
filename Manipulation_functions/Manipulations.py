# -*- coding: utf-8 -*-
"""
Created on Thu Jul  15 16:02:51 2021

@author: Manikantan Srinivasan and Rajat Mishra
"""

#importing the neccessary libraries
import sys
from PIL import Image,ImageOps
from pyzbar.pyzbar import decode
import math
from helper_functions import colorTemperatureToRGB,convert_temp
import math

'''The resolution function below reduces the factor of resolution by i for every iteration to check pyzbar's limits'''


def Resolution(image):
        open("txt_files/resolution.txt","w").close()
        res = []
        ppi_list = []
        wid, hgt = image.size
        print(str(wid) + "x" + str(hgt))
        for i in range(1,sys.maxsize):
            width = wid/i
            height = hgt/i
            image_i = image.resize((int(width),int(height)),Image.ANTIALIAS)
            res.append([width,height])
            image_i.save("combined_samples/resolution.jpeg",quality=95)
            decoded = decode(image_i)
            if(i==1):
                width_inches = 5.23622
                height_inches = 0.0787402
                diagonal_inches = math.sqrt((width_inches)**2+(height_inches)**2)
            if(decoded == []):
                diagonal_pixels = math.sqrt((wid/i)**2+(hgt/i)**2)
                ppi = diagonal_pixels/diagonal_inches
                ppi_list.append(ppi)
                print("barcode not found for resolution: "+ str(int(wid/i))+"x"+str(int(hgt/i)))
                break
            else:
                diagonal_pixels = math.sqrt((wid/i)**2+(hgt/i)**2)
                ppi = diagonal_pixels/diagonal_inches
                ppi_list.append(round(ppi,2))
                val = str(int(wid/i))+ "x" +str(int(hgt/i))
                
                file = open("txt_files/resolution.txt","a")
                file.write(val+" ppi: "+str(ppi)+"\n")
                file.close()
        return res,ppi_list
            
'''the Overlay_background function prints the straw/refill with the barcode info on the background images used during call'''


def Overlay_background(image,background):
    output_path = "combined_samples/background.jpeg"
    width = 1600
    height = 1200
    size = width,height
    barcode = image
    width_barcode,height_barcode = barcode.size
    if(width_barcode>width):
        size_barcode = width,height_barcode
        barcode_resized = barcode.resize(size_barcode,Image.ANTIALIAS)
        barcode_resized.save("temp/straw_resized.jpeg","JPEG")
        barcode = Image.open("temp/straw_resized.jpeg")
    background_resized = background.resize(size, Image.ANTIALIAS)
    background_resized.save("temp/background_resized.jpeg", "JPEG")
    background = Image.open('temp/background_resized.jpeg')
    if(width_barcode>width):
        background.paste(barcode,(width//6,height//2))
        background.save(output_path)
    else:
        background.paste(barcode,(width//6,height//2))
        background.save(output_path)
    if(decode(background)==[]):
        print('barcode not found for background')
    else:
        print('barcode found for background')
        
    decoded = decode(background)
    open("txt_files/background.txt","w").close()
    file1 = open("txt_files/background.txt","a")
    file1.write("barcode details for background used: "+ str(decoded)+"\n")
    file1.close()
    return background
    
'''This function takes the image and applies a lighting effect of different color temperatures'''


def Temperature(image,temp):
    r,g,b = colorTemperatureToRGB(temp)
    converted_image = convert_temp(image,r,g,b)
    converted_image.save("combined_samples/combined_temp.jpeg")
    if(decode(converted_image)==[]):
        print("barcode not found for temp: ",temp)
    else:
        print("barcode found for temp: ",temp)
        decoded  = decode(converted_image)
        open("txt_files/temp.txt","w").close()
        file = open("txt_files/temp.txt","a")
        file.write("barcode details for temperature: "+ str(decoded)+"\n")
    return converted_image
    
    
'''This function flips the image passed making it appear upside down'''

def Flip(image):
    output_path = "combined_samples/flip.jpeg"
    im_flip = ImageOps.flip(image)
    im_flip.save(output_path,quality=95)
    if(decode(im_flip)==[]):
        print("barcode not found for flip")
    else:
        print("barcode found for flip")
        decoded  = decode(im_flip)
        open("txt_files/flip.txt","w").close()
        file = open("txt_files/flip.txt","a")
        file.write("barcode details for flip: "+ str(decoded)+"\n")
    return im_flip
    
'''This function mirrors the image making it appear as a reflection from a mirror'''

def Mirror(image):
    output_path = "combined_samples/mirror.jpeg"
    im_mirror = ImageOps.mirror(image)
    im_mirror.save(output_path,quality=95)
    if(decode(im_mirror)==[]):
        print("barcode not found for mirror")
    else:
        print("barcode found for mirror")
        decoded  = decode(im_mirror)
        open("txt_files/mirror.txt","w").close()
        file = open("txt_files/mirror.txt","a")
        file.write("barcode details for mirror: "+ str(decoded)+"\n")
    return im_mirror
