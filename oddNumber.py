
def  oddnumber(x,y):
    for i in range(x,y+1):
        if i%2 != 0:
            print(i)

x = int(input('enter the value of x'))
y = int(input('enter the value of y'))

print('X value is ',x)
print('Y value is ',y)

oddnumber(x,y)