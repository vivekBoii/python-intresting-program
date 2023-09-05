from PIL import Image

image = Image.open(r"C:\Users\yadav\OneDrive\Desktop\vivek\python-intresting-program\images\4k\4k_5.jpeg")

newsize = (1600, 1200)

im1 = image.resize(newsize)
im1.show()
# try for jpeg if not then jpg 
image.save(im1,"jpg")
# save in temp storage
