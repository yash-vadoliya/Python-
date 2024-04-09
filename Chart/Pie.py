import matplotlib.pyplot as plt

prod_sales = [24,36,29,11]
prod_name = ['Sadan','Hatchback','Premium','Commercial']
col = ['teal','green','red','blue']

plt.pie(prod_sales,labels=prod_name,colors=col)
plt.pie(prod_sales,labels=prod_name)
plt.title('TATA Motors')

plt.legend()
plt.show()