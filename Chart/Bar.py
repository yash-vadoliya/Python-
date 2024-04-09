import xlrd
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('emp.xlsx')
print(df)

x = df['emp_name']
y = df['salary']

plt.bar(x,y,label="Emp Details",color="teal")
plt.xlabel("Emp Name")
plt .ylabel("Emp salary")

plt.title("Emp Details ")
plt.legend()
plt.show()