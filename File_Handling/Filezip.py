# Zipping the contents of files

from zipfile import *
# f = ZipFile('file.zip','w',ZIP_DEFLATED) # or use ZIP_STORE
# f.write('download.jfif')
# f.write('Shop.bin')
# f.close()

# unzip file
unzip = ZipFile('file.zip','r')
unzip.extractall('F:\\Yash\\Python\\File_Handling')