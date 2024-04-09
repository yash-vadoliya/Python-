# # READ CSV FILE AND DISPLAY DATA IN THE FORM OF DATA FRAME

# import pandas as pd
# df = pd.read_csv('employee.csv')
# print(df)

# =================================================================

# # READ DATA FROM XLSX FILE AND DISPLAY DATA IN THE FORM OF DATA FRAME

# import pandas as pd
# import xlrd
# df = pd.read_excel('emp.xlsx')
# print(df)

# =================================================================

# # READ DATA FROM DICTIONARY AND DISPLAY DATA IN THE FORM OF DATA FRAME

# import pandas as pd
# stud = {'roll':[1,2,3,4,5,6,7,8,9,10],
#         'name':['yash','dhaval','abhi','raj','ajay','ram','rohan','prince','kevin','kevel'],
#         'city':['Junagadh','Dhasa','Ahmadabad','Junagadh','Gandhinager','Surat','Rajkot','Jamanager','Surat','Mumbai']
#         }
# # df = pd.DataFrame(stud,columns=['roll','name','city'])
# df = pd.DataFrame(stud)

# print(df)

# =================================================================

# # READ DATA FROM TUPLE AND DISPLAY DATA IN THE FORM OF DATA FRAME

# stud = [(1,'abc',50,40,45),
#         (2,'bcd',55,44,45),
#         (3,'cde',40,35,55),
#         (4,'def',45,50,40),
#         (5,'efg',40,50,45)
#         ]
# import pandas as pd
# df = pd.DataFrame(stud,columns=['Roll','Name','Exam-1','Exam-2','Exam-3'])
# print(df)

# =================================================================

#  READ DATA FROM XLSX FILE AND DISPLAY DATA USE SOME FUNCTIONS

import pandas as pd
import xlrd

df = pd.read_excel('emp.xlsx')
print(df)
# know the number of row and column
print(df.shape)
print("=================================================================")
# Display the first five records
print(df.head())
print("=================================================================")
# Display the first specify records in brackets
print(df.head(2))
print("=================================================================")
# Display the last five records
print(df.tail())
print("=================================================================")
print(df.tail(3))
print("=================================================================")
# display range of rows
print(df[2:4])
print("=================================================================")
# display data from specific column
print(df['emp_name'])
print("=================================================================")
# Display data in maximum salary
print(df['salary'].max())
print("=================================================================")