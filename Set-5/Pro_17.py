# 17. Demonstrate the use of: i). break and ii). pass.

num = 5
print("Break :")
for i in range(num):
    if i==3:
        break
    else:
        print(i)
    
print("Pass :")
for i in range(num):
    if i==4:
        pass
    print(i)