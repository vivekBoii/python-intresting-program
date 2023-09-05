from PIL import Image

import os

filename=r"C:\Users\yadav\OneDrive\Desktop\vivek\python-intresting-program\cricket"

lst=os.listdir(filename)

for index,image in enumerate(lst):
    input_name=filename+"\\"+image

    image= Image.open(input_name)
    # if image.mode == "RGBA":
    image=image.convert("RGB")

    out_put = f"C:\\Users\\yadav\\OneDrive\\Desktop\\vivek\\python-intresting-program\\cricket\\anime-{index}.pdf"

    image.save(out_put,"PDF")