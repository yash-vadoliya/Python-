# Read and Write in Binary file
# Read an Image and Write into Binary File

file_read = open('download.jfif','rb') # rb => Read Binary File
file_write = open('myimg.jfif','wb') # wb => Write Binary File
img = file_read.read()
file_write.write(img)
file_read.close()
file_write.close()