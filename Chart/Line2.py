import matplotlib.pyplot as plt

overs = ['10','20','30','40','50']
Run_Team_A = [90,150,100,200,250]
Run_Team_B = [80,180,10,150,200]

plt.plot(overs,Run_Team_A,color='teal')
plt.plot(overs,Run_Team_B,color='orange')

plt.xlabel('Run In Overs')
plt.ylabel('Run Of Team')
plt.title('Team scores')

plt.show()