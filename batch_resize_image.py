#!/usr/bin/env python3
import os
from PIL import Image
'''@author partaze aka Cheryl'''

def create_list(source):
    '''Create a list of current image files within a specified folder'''
    my_list = []
    for file in os.listdir(source):
        absp = os.path.join(source, file)
        my_list.append(absp)
    names = [file for file in os.listdir(source)]
    return my_list,names



def process_images(ilist,nlist,dest):
    '''Iterate through the given list of image files, rotate by 90degrees clockwise,resize and save to the given path'''
    c=0
    for image in ilist:
        name = nlist[c]
        dest1 = os.path.join(dest, name)
        c+=1
        with Image.open(image) as im:
            im1 = im.rotate(90).resize((128,128)).convert('RGB')
            try:
                im1.save(dest1, 'JPEG')
            except Exception as e:
                print(e)

def get_path():
    source = input("Enter path of the source directory...")
    destination = input("Enter path of the destination directory..")
    return source,destination

if __name__=='__main__':
    source,destination = get_path()
    try:
        image_list,name_list = create_list(source)
        process_images(image_list,name_list,destination) 
    except:
        print("Oops!Something went wrong.")
        print("Please check the source and destination paths.")
