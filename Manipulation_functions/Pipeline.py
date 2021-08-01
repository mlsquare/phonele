# -*- coding: utf-8 -*-
"""
Created on Thu Jul  15 16:02:51 2021

@author: Manikantan Srinivasan and Rajat Mishra
"""

'''importing the neccessary libraries'''
from PIL import Image
from Manipulations import Resolution,Overlay_background,Temperature,Flip,Mirror
from pyzbar.pyzbar import decode

'''the pipeline function uses the functions from Manipulations.py in the order of Resolution-->Overlay_background-->temperature-->Mirror-->Flip to combine all effects and detect for the barcode'''


def pipeline(straws,backgrounds,temps,mirrors,flips):
    open("txt_files/data.txt","w").close()
    for straw in range(len(straws)):
        string_straw = ""
        image = Image.open(straws[straw]).convert("RGB")
        res,ppi = Resolution(image)
        string_straw= straws[straw]+","
        for i in range(len(ppi)):
            resized_generated = image.resize((int(res[i][0]),int(res[i][1])),Image.ANTIALIAS)
            string_resized= str(ppi[i])+","
            for background in range(len(backgrounds)):
                if(backgrounds[background]=="NA"):
                    background_generated = resized_generated
                    string_background= "NA"+","
                else:
                    string_background = ""
                    background_generated = Overlay_background(resized_generated,Image.open(backgrounds[background]))
                    string_background = backgrounds[background]+","
                for temp in range(len(temps)):
                    if(temps[temp]=="NA"):
                        temp_generated = background_generated
                        string_temp= "NA"+","
                    else:
                        string_temp = ""
                        temp_generated = Temperature(background_generated,temps[temp])
                        string_temp += str(temps[temp])+","
                    for mirror in range(len(mirrors)):
                        string_mirror = ""
                        if(mirrors[mirror]==True):
                            mirror_generated = Mirror(temp_generated)
                            string_mirror += str(mirrors[mirror])+","
                        else:
                            mirror_generated = temp_generated
                            string_mirror += str(mirrors[mirror])+","
                        for flip in range(len(flips)):
                            string_flip = ""
                            if(flips[flip]==True):
                                flip_generated = Flip(mirror_generated)
                                string_flip += str(flips[flip])+","
                            else:
                                flip_generated = mirror_generated
                                string_flip += str(flips[flip])+","
                            string_input = string_straw +string_resized+string_background + string_temp +string_mirror + string_flip
                            if(decode(flip_generated)==[]):
                                string_input += "failure"
                            else:
                                string_input += "success"
                            file = open("txt_files/data.txt","a")
                            file.write(string_input+"\n")
                               
