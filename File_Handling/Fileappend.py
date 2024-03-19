# Program to create a new file and write into existing file

f = open('file.txt','a') # a => Append mode..

str = input('Enter Data You Want To Enter Append In File =>')

f.write(str)

f.close() 
