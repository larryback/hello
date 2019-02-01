import openpyxl
# insert image
<<<<<<< HEAD
imgFile = './images/aaa.png'
=======
imgFile = './crawl/images/aaa.png'
>>>>>>> 14b1a64526eeb51aecda34d9ad38c7642b2542db
img = openpyxl.drawing.image.Image(imgFile)
sheet1.add_image(img, 'B5')
# resize image
from PIL import Image
img2 = Image.open(imgFile)
new_img = img2.resize((50, 50))
new_img.save('new.png')
img3 = openpyxl.drawing.image.Image(new_img)
sheet1.add_image(img3, 'B5')
