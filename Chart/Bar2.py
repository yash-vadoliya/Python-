import matplotlib.pyplot as plt

x = [101,103,106,108,110]
y = [10010,11109,20030,25002,31010]

x1 = [102,104,105,109,107]
y1 = [20110,31109,35004,29001,40000]

plt.bar(x,y,label='Production Department',color='teal')
plt.bar(x1,y1,label='QA Department',color='blue')

plt.xlabel('Employee ID')
plt.ylabel('Employee Salary')

plt.title('TATA Consultancy Service')

plt.legend()
plt.show()