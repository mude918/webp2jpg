from PIL import Image
import imghdr
import os

image_folder = './webp-images/'  
file_names = os.listdir(image_folder) 

for file_name in file_names: 
    if file_name[0] != '.': 
        filepath = image_folder + file_name
        filesuffix = (image_folder + file_name).split('.')[-1]
        trueformat = imghdr.what(image_folder + file_name)
        if filesuffix != trueformat:
            os.rename(filepath, '.'.join((image_folder + file_name).split('.')[:-1])+'.'+trueformat)
        if trueformat == 'webp':
            im = Image.open(image_folder + file_name).convert("RGB")
            im.save(image_folder + file_name, "jpeg")
            print('WEBP image: ', file_name)
        else:
            print(filesuffix, trueformat)
