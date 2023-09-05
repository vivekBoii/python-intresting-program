import os

lst=os.listdir(f"cricket")
path=r"C:\Users\yadav\OneDrive\Desktop\vivek\python-intresting-program\cricket\\"
for ind,file in enumerate(lst,start=1):
    if(file.endswith(".png")):
        old_name=path+file
        new_name=path+ "png_files_" + str(ind) + ".jpeg"
        os.rename(old_name,new_name)