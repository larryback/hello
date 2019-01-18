import openpyxl
# insert image
imgFile = './crawl/images/aaa.png'
img = openpyxl.drawing.image.Image(imgFile)
sheet1.add_image(img, 'B5')
# resize image
from PIL import Image
img2 = Image.open(imgFile)
new_img = img2.resize((50, 50))
new_img.save('new.png')
img3 = openpyxl.drawing.image.Image(new_img)
sheet1.add_image(img3, 'B5')
