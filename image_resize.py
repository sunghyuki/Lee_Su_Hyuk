from PIL import Image
import os

image_path = "./images/"

for new_file in os.listdir(image_path) :
    name_split = new_file.split('.')
    image_name = name_split[0] + '.jpg'
    im = Image.open(image_path+image_name)
    out = im.resize((300,300), Image.ANTIALIAS)
    out.save(image_path+image_name, dpi=(300,300))

