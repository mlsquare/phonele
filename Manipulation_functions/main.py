# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:28:00 2021
d
@author: Manikantan Srinivasan and Rajat Mishra
"""

from Pipeline import pipeline

def main():
    straws = ["straws/orange.jpeg"] # give the input of your choice for the straw image (user input required in place of "straws/orange.jpeg"
    backgrounds = ["backgrounds/black.jpeg"] #same as above for background
    temps = [5000] # same as above for color temperature to manipulation lighting effects
    flips = [True] #whether the image be flipped or not
    mirrors = [False] #whether the image be mirrored or not
    open("txt_files/data.txt","w").close()
    
    #calling the pipeline function from Pipeline.py 
    pipeline(straws,backgrounds,temps,mirrors,flips)
    
    
if __name__== "__main__":
    main()
