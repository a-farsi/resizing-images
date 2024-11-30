# import required module 
from PIL import Image 

# get image 
filepaths = ["original_images/Pakketlabel_naar_Duitsland_10-20_kg.png",  "original_images/Pakketlabel_naar_Duitsland_20+_kg.png", "original_images/rot90_Pakketlabel_naar_Duitsland_10-20_kg.png", "original_images/rot90_Pakketlabel_naar_Duitsland_20+_kg.png"]

for image in filepaths:
    print(f"Image name : {image}")
    img = Image.open(image)
    width = img.width
    height = img.height
    print("The height of the image is: ", height)
    print("The width of the image is: ", width)
