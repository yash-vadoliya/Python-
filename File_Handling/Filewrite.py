# Program to create a new file and write into file

# open or create a file.
f = open('File.txt','w') # w => write mode..

# get user input for write a file.
str = input('Enter Data You Want To Enter In File =>')

f.write(str) # using write() function write into file

f.close() # close the open file.