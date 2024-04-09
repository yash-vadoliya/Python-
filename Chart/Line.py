import matplotlib.pyplot as plt

years = ['2023', '2022', '2021', '2020', '2019','2018','2017','2016','2015','2014']
incre_pop = [89,78,55,80,95,80,78,75,60,80]

plt.plot(years,incre_pop,color='teal')

plt.title('Population Growth Of India')
plt.xlabel('Yrars')
plt.ylabel('Increase of Population in Lakhs')
plt.show()