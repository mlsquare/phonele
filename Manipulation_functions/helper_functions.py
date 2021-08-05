# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 19:01:18 2021

@author: mani
"""

'''helper functions of color temperature manipulation'''

from PIL import Image
from pyzbar.pyzbar import decode
import math


    
def clamp( x, min, max ):

    if(x<min):
        return min
    if(x>max):
        return max

    return x


def colorTemperatureToRGB(kelvin):
    temp = kelvin / 100
    
    

    if( temp <= 66 ): 

        red = 255
        
        green = temp
        green = 99.4708025861 * math.log(green) - 161.1195681661

        if( temp <= 19):

            blue = 0

        else:
            blue = temp-10
            blue = 138.5177312231 * math.log(blue) - 305.0447927307

        

    else:

        red = temp - 60
        red = 329.698727446 * math.pow(red, -0.1332047592)
        
        green = temp - 60;
        green = 288.1221695283 * math.pow(green, -0.0755148492 )

        blue = 255

    


     
    r = clamp(red,   0, 255)
    g = clamp(green, 0, 255)
    b = clamp(blue,  0, 255)
    return r,g,b

    



def convert_temp(image,r_input,g_input,b_input):
    r, g, b = r_input,g_input,b_input
    matrix = ( r / 255.0, 0.0, 0.0, 0.0,
             0.0, g / 255.0, 0.0, 0.0,
             0.0, 0.0, b / 255.0, 0.0 )
    return image.convert('RGB', matrix)
    

    
       

