import os

from PyPDF2 import PdfMerger

file_path=r"C:\Users\yadav\OneDrive\Desktop\vivek\python-intresting-program\cricket"

lst=os.listdir(file_path)
target_files=[]

# making list of pdf file
for file in lst:
    if(file.endswith(".pdf")):
        path=file_path+"\\"+file
        target_files.append(path)

merger=PdfMerger()

for pdf in target_files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()